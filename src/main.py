from flask import Flask, send_from_directory
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# // https://flask.palletsprojects.com/en/2.1.x/quickstart/#variable-rules

@app.route('/idem/<val>')
def idem(val):
    return f"val: {escape(val)}"

@app.route('/idem-int/<int:n>')
def idem_int(n: int):
    return f"n={n}"

