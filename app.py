from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

# ===========================================
# ROUTES
# ===========================================

# ===========================================
# RUN
# ===========================================
if __name__ == '__main__':
    app.debug = True
    app.run()
