from flask import Flask, render_template, session, request, redirect, url_for
from utils import auth
from nutritionix import Nutritionix
import json

# apikeys[0] - nutirinoix key - "070678e0943ef0af60625a44d7de3bb3"
f = open("keys.txt","r") #opens file with name of "test.txt"
apikeys = []
for line in f:
    key = line.strip('\n')
    apikeys.append(key)
nix = Nutritionix(app_id="b31ef4ce", api_key=apikeys[0])
app = Flask(__name__)

# ===========================================
# ROUTES
# ===========================================
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route("/authenticate/", methods = ["GET", "POST"])
def authenticate():
    if 'register' in request.form.keys():
        if not request.form['username'] or not request.form['password']:
            msg = "Please enter a username and password."
        elif auth.register(request.form['username'], request.form['password']):
            msg = "Successfully registered!"
        else:
            msg = "Failed to register! Username is taken."
        return render_template("authenticate.html", register_message = msg)

    elif 'login' in request.form.keys():
        if not request.form['username'] or not request.form['password']:
            msg = "Please enter a username and password."
        elif auth.login(request.form['username'], request.form['password']):
            session["user"] = request.form['username']
            return redirect(url_for("profile"))
        else:
            msg = "Failed to login. Username and/or password incorrect."
        return render_template("authenticate.html", login_message = msg)

    else:
        return render_template("authenticate.html")

        
@app.route('/profile/')
def profile():
    if 'user' in session:
        return render_template('profile.html')
    else:
        return redirect(url_for("home"))    

@app.route('/display/', methods = ["GET", "POST"])
def display():
    d = []
    if 'search' in request.form.keys():
        if not request.form['lookup']:
            return redirect(url_for("home"))
        else:
            call = nix.search(request.form['lookup'], results="0:5").json()
            call = call['hits']
	#    for i in call:
	#	d[i] = call[i]		    
            #for index in call:
	#	id = call[index]["_id"]
	#	d[index] = nix.item(id).json()	
            #call = nix.item(id=call).json()
            return render_template('display.html', fooddata = call, foodname=request.form['lookup'])
    else:
        return redirect(url_for("home"))

@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

# ===========================================
# RUN
# ===========================================

if __name__ == '__main__':
    app.debug = True
    app.config.from_object('config')
    app.secret_key = app.config['SECRET_KEY']
    app.run()
