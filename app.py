from flask import Flask, render_template, session, request, redirect, url_for

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
    if 'submit' not in request.form:
        return render_template("authenticate.html")

    if request.form['submit'] == 'register':
        if not request.form['username'] or not request.form['password']:
            msg = "Please enter a username and password."
        elif auth.register(request.form['username'], request.form['password']):
            msg = "Successfully registered!"
        else:
            msg = "Failed to register! Username is taken."
        return render_template("authenticate.html", message = msg)

    elif request.form['submit'] == 'login':
        if not request.form['username'] or not request.form['password']:
            msg = "Please enter a username and password."
        elif auth.login(request.form['username'], request.form['password']):
            session["user"] = request.form['username']
            return redirect(url_for("profile"))
        else:
            msg = "Failed to login. Username and/or password incorrect."
        return render_template("authenticate.html", message = msg)

@app.route('/profile/')
def profile():
    if 'user' in session:
        return render_template('profile.html')
    else:
        return redirect(url_for("home"))

@app.route('/display/')
def display():
    return render_template('display.html')

# ===========================================
# RUN
# ===========================================
if __name__ == '__main__':
    app.debug = True
    app.run()
