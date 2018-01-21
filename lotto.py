import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Server parameters
CLIENT_SIDE_URL = "http://18.216.149.158"
PORT = 8080

@app.route("/")
def gate():
    return render_template("gate.html")

@app.route("/entry")
def entry():
    return render_template("entry.html")

@app.route("/lotto")
def lotto():
    return render_template("lotto.html")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, threaded=True, port=PORT)
    app.run(host="localhost", debug=True, port=PORT)
