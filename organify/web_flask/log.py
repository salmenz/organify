#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from models import storage
from models.user import User
from models.post import Post
from models.comment import Comments
from models.interview import Interview
from models.answer import Answer
from models.correction import Correction
from models.category import Category
from models.subcategory import Subcategory
from models.sub_follow import Sub_follow
from models.relation import Relation
from models.comm_like import Comm_like
from models.post_like import Post_like
from models.question import Question
from web_flask import app


app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'job_dev'
app.config['MYSQL_PASSWORD'] = 'job_dev_pwd'
app.config['MYSQL_DB'] = 'job_win_db'

# Intialize MySQL
mysql = MySQL(app)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE username = %s AND passwd = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return render_template('profile.html', msg=msg)
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

