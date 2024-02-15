from flask import Blueprint,render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import mysql.connector
from datetime import timedelta

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/authentication/static')

auth.secret_key = 'r$W9#kLp2&QnX@5*8yZ$'

mysql = MySQL()
# Initialize MySQL
def init_mysql_auth(app):
    mysql.init_app(app)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '@Arvi7777'
    app.config['MYSQL_DB'] = 'ceo-application'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'userName' in request.form and 'password' in request.form:
        print("infunction")
        username = request.form['userName']
        password = request.form['password']
        hash = password + auth.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM `ceo_login_database` WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return the revenue_result
        ceo_login_database = cursor.fetchone()
        print(ceo_login_database)
        # If account exists in accounts table in out database
        if ceo_login_database:
            # Create session data,to access this data in other routes
            session['loggedin'] = True
            session['id'] = ceo_login_database['id']
            session['username'] = ceo_login_database['username']
            # Redirect to home page
            # return redirect (url_for('landingPage'))
            return "success"
        else:
            # username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg='')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and 'firstName' in request.form and 'userName' in request.form and ('password' and 'confirmPassword') in request.form and 'phoneNumber' in request.form and 'emailID' in request.form:
        firstname = request.form['firstName']
        if (request.form['lastName']):
            lastname = request.form['lastName']
        else:
            lastname = ""
        username = request.form['userName']
        password = request.form['password']
        confirmpassword = request.form['confirmPassword']
        countrycode = request.form['countryCode']
        phonenumber = request.form['phoneNumber']
        phonenumber = countrycode + phonenumber
        emailID = request.form['emailID']
        if (request.form['gender']):
            gender = request.form['gender']
        else:
            gender = ""

        print(firstname,lastname,username,password,confirmpassword,phonenumber,emailID,gender)
    return render_template('signup.html')