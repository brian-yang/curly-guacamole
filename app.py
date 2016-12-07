from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

# ===========================================
# ROUTES
# ===========================================
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/authenticate/')
def auth():
    return render_template('authenticate.html')

@app.route('/profile/')
def profile():
    return render_template('profile.html')

@app.route('/display/')
def display():
    return render_template('display.html')

# ===========================================
# RUN
# ===========================================
if __name__ == '__main__':
    app.debug = True
    app.run()
