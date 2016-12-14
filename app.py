from flask import Flask, render_template, session, request, redirect, url_for
from utils import auth
import json, urllib2

# apikeys[0] - nutirinoix key - "070678e0943ef0af60625a44d7de3bb3"
f = open("keys.txt","r") #opens file with name of "test.txt"
apikeys = []
for line in f:
    key = line.strip('\n')
    apikeys.append(key)
app = Flask(__name__)

#http://api.nal.usda.gov/ndb/search/?format=json&q=butter&sort=n&max=25&offset=0&api_key=DEMO_KEY

k = apikeys[0]

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
    d = {}
    ar = []
    if 'search' in request.form.keys():
        if not request.form['lookup']:
            return redirect(url_for("home"))
        else:
            url = "http://api.nal.usda.gov/ndb/search/?format=json&q=%s&sort=n&max=%d&offset=0&api_key=%s"%(request.form["lookup"], 5, k)
            
            jsonf = urllib2.urlopen(url).read()
            jsonf = json.loads(jsonf)
            jsonf = jsonf["list"]["item"]
            #print jsonf 
            #list of dictionaries

            for index in jsonf:
                nutri = "http://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=%s&nutrients=205&nutrients=204&nutrients=208&nutrients=269&nutrients=291&nutrients=301&nutrients=303&nutrients=431&nutrients=304&nutrients=305&nutrients=306&nutrients=307&nutrients=401&nutrients=415&nutrients=418&nutrients=320&ndbno=%s"%(k,index["ndbno"])
                nutrif = json.loads(urllib2.urlopen(nutri).read())
                d[index["name"]] = nutrif["report"]["foods"][0]["nutrients"]
                        
            
            return render_template('display.html', fooddata = d, foodname=request.form['lookup'])
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
