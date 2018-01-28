import flask
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug import secure_filename

app = Flask(__name__)
Bootstrap(app)

# Server parameters
CLIENT_SIDE_URL = "http://18.216.149.158"
PORT = 8080

@app.route("/")
def gate():
    return render_template("upload.html")

@app.route("/lotto", methods=['POST'])
def lotto():
    # Do some error checking
    if ('pass' not in request.form or not request.form['pass']):
        return render_template("error.html")

    # Match the password
    if request.form['pass'] != 'mississippi':
        return render_template("error.html")

    # Save the file
    f = request.files['file']
    f.save(secure_filename("entries.txt"))

    # Read in the array
    entries = []
    for entry in open("entries.txt"):
        entries.append(entry.rstrip())

    return render_template("lotto.html", entries=entries)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, threaded=True, port=PORT)
    app.run(host="localhost", debug=True, port=PORT)
