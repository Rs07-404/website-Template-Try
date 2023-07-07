from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    time = datetime.now()
    hour = int(time.strftime("%H"))
    if 0 < hour < 12:
        greet = f"Good Morning"
    elif 12 < hour < 17:
        greet = f"Good Afternoon"
    elif 17 < hour < 24:
        greet = f"Good Evening"
    else:
        greet = "Good Go!"
    return render_template("index.html", greet=greet)

@app.route('/blog')
def show_blog():
    pass

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signup/successful', methods = ["POST"])
def success():
    email = request.form["email"]
    password = request.form["password"]
    return f"<h1>Email: {email}, Password: {password}</h1>"


app.run(debug = True)
