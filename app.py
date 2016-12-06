from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

# ===========================================
# ROUTES
# ===========================================
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/auth/')
def auth():
    return render_template('authenticate.html')

# ===========================================
# RUN
# ===========================================
if __name__ == '__main__':
    app.debug = True
    app.run()
