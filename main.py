import os

from flask import Flask, render_template


KEY = "AIzaSyCU8AOyOFfPBH5aZnphqXhg6aeD6dix0nk"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", key=KEY)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)