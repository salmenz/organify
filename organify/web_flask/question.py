#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/question')
def hello_hbnb():
    """ Prints a Message when / is called """
    return render_template('questions.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
