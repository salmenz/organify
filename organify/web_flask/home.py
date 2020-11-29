#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from models import storage
from models.user import User
from models.post import Post
from models.question import Question
from models.answer import Answer
from models.calendar import Calendar
from web_flask import app






# Change this to your secret key (can be anything, it's for extra protection) 
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cal_dev'
app.config['MYSQL_PASSWORD'] = 'cal_dev_pwd'
app.config['MYSQL_DB'] = 'cal_win_db'


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
            return redirect(url_for('profile', msg=msg))
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

@app.route('/')
@app.route('/home')
def home():
    """ Prints a Message when / is called """
    if not session:
        users = storage.all(User).values()
        posts = storage.all(Post).values()
        comments = storage.all(Comments).values()
        return render_template('home.html', users=users, posts=posts, coms=comments)
    else:
        return redirect(url_for('user-home'))

@app.route('/signup')
def signup():
    """ signup  """
    if not session:
        return render_template('signup.html')
    else:
        return redirect(url_for('user-home'))

@app.route('/contact_us')
def contact_us():
    """contact us"""
    if session:
        return redirect(url_for('contact_us_user'))
    else:
        return render_template('contact_us.html')


@app.route('/contact_us_user')
def contact_us_user():
    """contact us"""
    if session:
        return render_template('contact_us_user.html')
    else:
        return redirect(url_for('contact_us'))



@app.route('/profile')
def profile():
    """profile"""
    if session:
        st = storage.all('User').values()
        id = session['id']
        lista = []
        for user in st:
            if user.id == id:
                lista = user
        followers = storage.all('Relation').values()
        posts = storage.all('Post').values()
        comments = storage.all('Comments').values()
        users = storage.all('User').values()
        return render_template('profile.html', user_id=id, user=lista, followers=followers,
        posts=posts, comments=comments, users=users)
    else:
        return jsonify({"Error": "Not found"})


@app.route('/questions')
def question():
    """interview"""
    if session:
        return render_template('questions.html')
    else:
        return jsonify({"Error": "Not found"})



@app.errorhandler(404)
def page_404(e):
    """ Return a custom 404 error """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
