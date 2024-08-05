from flask import Flask, request, render_template, jsonify
from love_calc import calculator

app = Flask(__name__)


#_________________________________________Routing Methods_________________________________________
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/love', methods=['POST'])
def solve():
    try:
        name1 = request.form['name1']
        name2 = request.form['name2']
        percent = calculator(name1, name2)
        return jsonify(percent)
    except:
        return 0


#______run app__________
if __name__=="__main__":
    app.run(debug=True)
