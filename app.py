from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(128)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index(): # this function generates the session using the connection attempt from the customer

    session["grant_url"] = request.args.get('base_grant_url')
    session["user_continue_url"] = request.args.get('user_continue_url')

    return render_template('captive_portal.html')


@app.route('/connected')
def good():

    if not session["grant_url"] == None:
        # this code will run if the grant_url exists and redirect the user to their original destination
        print("-------- "+ session["grant_url"])
        original_url = session["grant_url"]+"?continue="+session["user_continue_url"]
    else:
        # Enter the link to the desired redirect page if the end-user didn't connect with a continue_url
        return redirect('https://www.example.com/')
    return redirect(original_url, code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
