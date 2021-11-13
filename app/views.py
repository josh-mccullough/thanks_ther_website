from flask import request, render_template, session, redirect
from app import app


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        return "Get"
    else:
        print("neither post or get, im confused")


@app.route('/blogs', methods=["GET", "POST"])
def blogs():
    if request.method == "GET":
        return render_template("blogs.html")


@app.route('/transcripts', methods=["GET", "POST"])
def transcripts():
    if request.method == "GET":
        return render_template("transcripts.html")


@app.route('/about', methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")


@app.route('/shop', methods=["GET", "POST"])
def shop():
    if request.method == "GET":
        return render_template("shop.html")
