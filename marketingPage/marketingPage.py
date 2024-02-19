from flask import Flask, Blueprint, session, render_template, redirect, url_for
import mysql.connector

marketingPage = Blueprint('marketingPage', __name__, template_folder='templates', static_folder='static', static_url_path='/marketingPage/static')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Arvi7777",
    database="ceo-revenue"
)

@marketingPage.route('/marketing-module')
def marketingModule():
    if 'loggedin' in session:
        if session['role'] == "Guest":
            return redirect(url_for('auth.login', msg = f"As a {session['role']}, you do not have access to login."))
        elif session['role'] == "Employee":
            return render_template('marketingPage.html',
                                username = session['username'],
                                email = session['email'],
                                role = session['role'],
                                month = [],
                                revenue = [],
                                profit = [],
                                expense = [],
                                msg=f"You are not authorized to view this page.")
        cursor = mydb.cursor()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # Initializing the total revenue for each month
        total_revenue, payment_type, payment_mode = {} , [] , [0,0,0]
        for table in months:
            total_revenue[table] = 0
        # Iterate over the months and get the sum of revenue for each month
        for table in months:
            sql_revenue = f"""
            SELECT SUM(revenue) AS revenue, SUM(profit) AS profit, SUM(expense) AS expense
            FROM  {table}
            """
            cursor.execute(sql_revenue)
            revenue_result = cursor.fetchone()
            total_revenue[table] = revenue_result
        month, revenue, expense, profit = [] , [] , [] , []
        # Print the total revenue for each month
        for mon, total_revenue in total_revenue.items():
            month.append(mon)
            revenue.append(f'{total_revenue[0]}')
            expense.append(f'{total_revenue[1]}')
            profit.append(f'{total_revenue[2]}')
        # Close the cursor and database connection
        cursor.close()
        return render_template('marketingPage.html',
                                username = session["username"],
                                email = session['email'],
                                role = session['role'],
                                month = month,
                                revenue = revenue,
                                expense = expense,
                                profit = profit)
    return redirect(url_for('auth.login'))
