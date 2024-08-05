from flask import Flask, render_template, request, session, redirect, url_for
from  flask_socketio import join_room, leave_room, send ,SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config['SECRET_KEY'] = '260704'
socketio = SocketIO(app)

rooms = {}
def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code+=random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code

@app.route('/', methods = ['POST', 'GET'])
def main():
    session.clear()
    if request.method == "POST":
        #Since We are Getting from a Dictionary, We can set a default value for KeyNotFoundError with the get method.
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)
        print(create)

        if not name:
            return render_template("home.html", error="Please enter a Name", name=name, code=code)
        
        if join !=False and not code:
            return render_template("home.html", error="Please enter a Code", name=name, code=code)
        
        room = code
        if create!=False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages":[]}
        elif code not in rooms:
            return render_template("home.html", error="Room Does Not Exist", name=name, code=code)

        session['room'] = room
        session['name'] = name
        return redirect(url_for("room"))

    return render_template("home.html")


@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect("/")
    return render_template("room.html", code=room, messages=rooms[room]["messages"])


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    room[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
     room = session.get("room")
     name = session.get("name")

     if not room or not name:
         return
     
     if room not in rooms:
         leave_room(room)
         return
     
     join_room(room)
     send({"name":name, "message":"has Entered the Room"}, to = room)
     rooms[room]["members"] += 1
     print(f"{name} Joined Room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")

    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -=1
        if  rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name":name, "message":"has Left the Room"}, to = room)
    print(f"{name} has left Room {room}")

if __name__ == "__main__":
    socketio.run(app, debug=True)