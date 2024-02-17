from flask import Blueprint, render_template,session, redirect, url_for
import mysql.connector

landingPage = Blueprint('landingPage', __name__, template_folder='templates', static_folder='static', static_url_path='/landingPage/static')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Arvi7777",
    database="ceo-revenue"
)

@landingPage.route('/landing-page')
def landingPageHome():
    if 'loggedin' in session:
        cursor = mydb.cursor()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # Initialize the total revenue for each month
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

            payment_type_sql = f"""
            SELECT '{table}' AS Month, 'Credit card' AS Payment_Type, COUNT(*) AS Occurrences FROM `ceo-revenue`.{table} WHERE payment_type = 'Credit card'
            UNION ALL
            SELECT '{table}' AS Month, 'Debit card' AS Payment_Type, COUNT(*) AS Occurrences FROM `ceo-revenue`.{table} WHERE payment_type = 'Debit card'
            UNION ALL
            SELECT '{table}' AS Month, 'UPI' AS Payment_Type, COUNT(*) AS Occurrences FROM `ceo-revenue`.{table} WHERE payment_type = 'UPI'
            ORDER BY Month, Payment_Type;
            """
            cursor.execute(payment_type_sql)
            payment_type_result = cursor.fetchall()

            payment_type.append(payment_type_result)
            total_revenue[table] = revenue_result
            month, revenue, expense, profit = [] , [] , [] , []

        # Print the total revenue for each month
        for mon, total_revenue in total_revenue.items():
            month.append(mon)
            revenue.append(f'{total_revenue[0]}')
            expense.append(f'{total_revenue[1]}')
            profit.append(f'{total_revenue[2]}')
        # Counting the Number of Credit, debit and UPI users
        for i in payment_type:
            for j in i:
                if j[1] == "Credit card":
                    payment_mode[0] += j[2]
                if j[1] == "Debit card":
                    payment_mode[1] += j[2]
                if j[1] == "UPI":
                    payment_mode[2] += j[2]

        # Close the cursor and database connection
        cursor.close()
        return render_template('landingPage.html',
                                username = session['username'],
                                month = month,
                                revenue = revenue,
                                profit = profit,
                                payment_mode = payment_mode)
    return redirect(url_for('auth.login'))