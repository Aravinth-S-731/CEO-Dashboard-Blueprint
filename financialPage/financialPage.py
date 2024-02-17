from flask import Flask, Blueprint, session, render_template, redirect, url_for
import mysql.connector

financialPage = Blueprint('financialPage', __name__, template_folder='templates', static_folder='static', static_url_path='/financialPage/static')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Arvi7777",
    database="ceo-revenue"
)

@financialPage.route('/financial-module')
def financialModule():
    if 'loggedin' in session:
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
        # Income Statement
        income_data = [
            ["Revenue", "₹ 40,330"],
            ["COGS", "₹ 2,017"],
            ["Gross Profit", "₹ 16,132"],
            ["OPEX", "₹ 1,613"],
            ["Sales", "₹ 2,419"],
            ["Marketing", "₹ 4,033"],
            ["General & Admin", "₹ 3,226"],
            ["Other Income", "₹ 1,209"],
            ["Other Expense", "₹ 4,330"],
            ["Operating Cost", "₹ 6,049"]
        ]
        return render_template('financialPage.html',
                                username = session['username'],
                                month = month,
                                revenue = revenue,
                                expense = expense,
                                profit = profit,
                                income_data = income_data,)
    return redirect(url_for('auth.login'))
