from flask import Flask, Blueprint, session, render_template, url_for, redirect
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

operationalPage = Blueprint('operationalPage', __name__, template_folder='templates', static_folder='static', static_url_path='/operationalPage/static')

mysql = MySQL()

def init_mysql_auth(app):
    mysql.init_app(app)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '@Arvi7777'
    app.config['MYSQL_DB'] = 'ceo-application'


@operationalPage.route('/operational-module')
def operationalModule():
    if session['role'] == "Guest":
        return redirect(url_for('auth.login', msg = f"As a {session['role']}, you do not have access to login."))
    elif session['role'] == "Client":
        return render_template('operationalPage.html',
                            username = session['username'],
                            email = session['email'],
                            role = session['role'],
                            employee_count_per_department = [],
                            average_salary_per_department = [],
                            salary_range_of_employee = [],
                            employess_gender_count = [],
                            msg=f"You are not authorized to view this page.")
    if 'loggedin' in session:
        # Variable decoration
        department_emp_counts = {
            'management': 0,
            'accounts': 0,
            'media': 0,
            'creative team': 0,
            'research': 0,
            'HR': 0,
            'IT': 0
        }
        department_avg_salary = {
            'management': 0,
            'accounts': 0,
            'media': 0,
            'creative team': 0,
            'research': 0,
            'HR': 0,
            'IT': 0
        }
        salary_range = {
            '0-20,000': 0,
            '20,001-40,000': 0,
            '40,001-60,000': 0,
            '60,001-80,000': 0,
            '80,001-1,00,000': 0,
        }
        emp_gender_count = {
            'male': 0,
            'female': 0
        }
        # DATABASE ACCESS
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM `employee_details`')
        emp_details = cursor.fetchall()
        # DATA EXTRACTION
        # FOR COUNT OF EMP IN EACH DEPT
        for emp in emp_details:
            department = emp['department']
            salary = emp['salary']
            department_emp_counts[department] += 1
            department_avg_salary[department] += salary

        # FOR AVENGE SALARY
        for department, count in department_emp_counts.items():
            department_avg_salary[department] = round(department_avg_salary[department] / count)

        # Extract the salaries from the 'emp_details' data
        salaries = [emp['salary'] for emp in emp_details]
        for i in salaries:
            if (i >= 0 and i <= 20000):
                salary_range['0-20,000'] += 1
            if (i >= 20001 and i <= 40000):
                salary_range['20,001-40,000'] += 1
            if (i >= 40001 and i <= 60000):
                salary_range['40,001-60,000'] += 1
            if (i >= 60001 and i <= 80000):
                salary_range['60,001-80,000'] += 1
            if (i >= 80001 and i <= 100000):
                salary_range['80,001-1,00,000'] += 1

        # Extract the genders from the 'emp_details' data
        genders = [emp['gender'] for emp in emp_details]
        for i in genders:
            if i == 'male':
                emp_gender_count["male"]+=1
            else:
                emp_gender_count["female"]+=1

        print(department_emp_counts)
        print(department_avg_salary)
        print(salary_range)
        print(emp_gender_count)
        return render_template('operationalPage.html',
                                username = session['username'],
                                email = session['email'],
                                role = session['role'],
                                employee_count_per_department = department_emp_counts,
                                average_salary_per_department = department_avg_salary,
                                salary_range_of_employee = salary_range,
                                employess_gender_count = emp_gender_count)
    return redirect(url_for('auth.login'))
