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
    msg = request.args.get('msg','')
    if request.method == 'POST' and 'userName' in request.form and 'password' in request.form:
        username = request.form['userName']
        password = request.form['password']
        hash = password + auth.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        print(password)
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

@auth.route('/verify-mail', methods = ["GET", "POST"])
def sendMail():
    session.pop('email', None)
    session.pop('otp', None)
    if  request.method == 'POST':
        mailID = request.form['mailID']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM `ceo_login_database` WHERE email = %s', (mailID,))
        ceo_login_database = cursor.fetchone()
        if ceo_login_database:
            msg = 'Account already exists!'
            return redirect(url_for('auth.login', msg = msg))
        otp = random.randint(1000,9999)
        session['email'] = mailID
        session['otp'] = otp
        return redirect(url_for('auth.otpValidation'))
    return render_template('verifyEmail.html')

@auth.route('/otpValidation', methods=['POST', 'GET'])
def otpValidation():
    emailID = session.get('email')
    otp = session.get('otp')
    print('Generated OTP: ', otp)
    mail_message = Message('Verify your mail-ID', sender = 'aravinth7871867225@gmail.com', recipients = [emailID])
    mail_message.body = f"Dear user,\n\nYour OTP for creating an account for CEO Dashboard is: {otp}\n\nPlease use this OTP to complete your account registration.\n\nThank you."
    mail.send(mail_message)
    msg = ''
    if request.method == 'POST':
        user_entered_otp = request.form['otp']
        print("User OTP:", user_entered_otp)
        if int(user_entered_otp) == otp:
            return redirect(url_for('auth.signup'))
        else:
            msg = 'Invalid OTP! Please register again.'
            return render_template('verifyEmail.html', msg=msg)
    return render_template('otpValidation.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ""
    emailID = session.get('email')
    print(emailID)
    if emailID == None:
        msg = 'Verify your mail first'
        return redirect(url_for('auth.sendMail', msg = msg))
    if request.method == 'POST' and 'firstName' in request.form and 'userName' in request.form and ('password' and 'confirmPassword') in request.form and 'phoneNumber' in request.form:
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
        if (request.form['gender']):
            gender = request.form['gender']
        else:
            gender = ""
        hash = password + auth.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        print(firstname,lastname,username,password,confirmpassword,phonenumber,emailID,gender)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO `ceo_login_database` (firstname, lastname, username, password, phonenumber, email, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)', (firstname, lastname, username, password, phonenumber, emailID, gender))
        mysql.connection.commit()
        cursor.close()
        print("User details inserted into the database")
        msg = 'Account Created Successfully. Please Login to Continue.'
        return redirect(url_for('auth.login', msg = msg))
        # return redirect(url_for('auth.otpValidation'),otp)
    return render_template('signup.html', msg = msg, mailID = emailID)