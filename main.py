import os

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/google3c8d8110329b8523.html')
def google_search_verify():
    return render_template("google3c8d8110329b8523.html")


@app.route('/history')
def history():
    dt = request.args['dt']
    template = dt + '.html'
    return render_template(template)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)