from flask import Blueprint,render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import mysql.connector
import random
from datetime import timedelta

from flask_mail import Mail, Message
auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/authentication/static')

auth.secret_key = 'r$W9#kLp2&QnX@5*8yZ$'

mail = Mail()
mysql = MySQL()
# Initialize MySQL
def init_mysql_auth(app):
    mysql.init_app(app)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '@Arvi7777'
    app.config['MYSQL_DB'] = 'ceo-application'
    
    app.config['MAIL_SERVER'] = "smtp.googlemail.com"
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = "aravinth7871867225@gmail.com"
    app.config['MAIL_PASSWORD'] = "hoijwhxxspatlmys"
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'userName' in request.form and 'password' in request.form:
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
            msg = "Invalid Username / Password"
    return render_template('login.html', msg = msg)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ""
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
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM `ceo_login_database` WHERE username = %s', (username,))
        ceo_login_database = cursor.fetchone()
        # If ceo_login_database exists show error and validation checks
        if ceo_login_database:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', emailID):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not emailID:
            msg = 'Please fill out the form!'
        else:
            print("upload process")
            generateOTP(firstname, emailID)
        print(msg)
        print(firstname,lastname,username,password,confirmpassword,phonenumber,emailID,gender)
    return render_template('signup.html')

def generateOTP(firstName, mailID):
    otp = random.randint(1000,9999)
    result = sendMail(otp, firstName, mailID)
    return print(result + "otp generation")

def sendMail(otp, firstName, mailID):
    mail_message = Message('Verify your mail-ID', sender = 'aravinth7871867225@gmail.com', recipients = [mailID])
    mail_message.body = f"Dear {firstName},\n\nYour OTP for creating an account is: {otp}\n\nPlease use this OTP to complete your account registration.\n\nThank you."
    mail.send(mail_message)
    return "Mail Sent Successfully"