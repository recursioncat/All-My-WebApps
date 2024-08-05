from flask import Flask, render_template, redirect, url_for, request, flash
import json
import os
from Backend_Scripts.VideoClasses import getPath
from Backend_Scripts.mail import send_mail


app = Flask(__name__)
app.secret_key = os.environ.get('Flask_Secret_Key')

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contacts():
    return render_template('contacts.html')

@app.route('/gallery')
def gallery():
    with open("Backend_Scripts/ListofVideos.json", 'r') as File:
        videolist = json.load(File)
    
    list_of_paths = [url_for('static', filename=f'Videos/{getPath(video["path"])}') for video in videolist]
    print("List of PAths: ", list_of_paths)
    return render_template('gallery.html', videolist=videolist,list_of_paths = list_of_paths)

@app.route('/process_query', methods = ['POST'])
def process_query():
    try:
        name = request.form.get('Name')
        phone_num = request.form.get('phone-number')
        email_id = request.form.get('email')
        query = request.form.get('query')
        mail_call = request.form.get('email-call')
        phone_call = request.form.get('phone-call')

        return_type = 'mail' if mail_call == 'on' else 'phone'

        body = f'''
            Name of Sender: {name}
            Phone Number: {phone_num}
            Sender Email: {email_id}
            Preffered Method of Reply: {return_type}
            Query:{query}
        '''

        send_mail('labonibanerjee99@gmail.com', 'New Query From Alaap', body)
        flash("Query Sent Successfully!", "success")
    
    except Exception as e:
        print(str(e))
        flash('Some Unknown Error Occurred', "error")
    
    return redirect(url_for('.contacts'))



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
