# CEO Dashboard
## OneYes InfoTech Solutions
This Web application is to create a CEO dashboard that will provide a comprehensive overview of key performance indicators (KPI), financial data and other relevant metrics to assist the CEO in making the informed decisions. This application has 6 - major functionalities to be met, these functionalities are,

#### 1. User Authentication and Authorization.
#### 2. Dashboard Overview.
#### 3. Financial metrics Module.
#### 4. Sales and Marketing Module.
#### 5. Operational Metrics Module.
#### 6. Collaboration and Communication Module.

---
---


## 1. User Authentication and Authorization
The Admin authentication module is responsible for validating the identity of users accessing the system. It includes features such as login, registration of accounts. Admin can login using the login module, If not they can also register a new account to login to the application. This module four functionality. They are,
### I. Login  Functionality
The login functionality allows users to authenticate themselves and gain access to the CEO Dashboard. This uses security key to encode and decode password. When the users login, the application verifies the login credentials with the database. The code block for login is given below.
```
@app.route('/login', methods=['GET', 'POST'])
if (credentials matches):
    Login
else:
    Redirect to login page
```
<!-- <img src="./Mark_ down_sources/Login-Page.png" style="width: 250px; border-radius: 10px;"> -->

### II. Registration Functionality
The user registration functionality allows new users to create accounts. It includes validation checks for username, password, and email. The credentials of the users is sent to the database and the user is redirected to the login page. [***NOTE :*** These login and registration module is vulnerable to SQL injection]. The code snippet for registration page is given below.
```
@app.route('/register', methods=['GET', 'POST'])
def register():
    if (details filled):
        Push to Database
    else:
        Throw error for Incomplete form
```
#### Accessability according to Roles
|Roles      |Home|Finance|Marketing|Operational|Chat|Logout|
|-----------|----|-------|---------|-----------|----|------|
|Admin      |   x|      x|        x|          x|   x|    o |
|Manager    |    |       |        x|          x|   x|    o |
|Employee   |    |       |         |          x|   x|    o |
|Client     |    |       |        x|           |    |    o |
|Guest      |  - |      -|        -|          -|   -|    o |

<!-- <img src="./Mark_ down_sources/Registration-Page.png" style="width: 250px; border-radius: 10px;"> -->

### III. Logout Functionality
The logout functionality clears the user's session data and redirects them to the login page. This options is available after the successful initiation of login process. The code for logout functionality is,
```
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
```

### IV. Session Management
The application uses Flask's session management to keep users logged in. Additionally, an automatic session timeout of 30 minutes is implemented for security purposes. The code to perform this functionality is given below.
```
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
```

---

## 2. Navigation Bar
Navigation bar of the web application enables the user / Admin to navigate to multiple modules of the dashboard without any trouble. The navigation bar has links to modules like Home, Finance, Marketing, Operational, Chat and Logout

<!-- <img src="/Mark_ down_sources/Navigation-Bar.png" style="height: 300px;"> -->
![Navigation Bar](Mark_%20down_sources/Navigation-Bar.png)

## 3. Dashboard Overview Module
**Dashboard** is the main interface of the application, where users can view their data, and come to a conclusion. This page contains details like,
- Revenue Generated per Month
- Mode of Revenue Generation
- Profit Earned throughout the Year
- Basic Account Details

---

## 4. Financial Metrics Module
The Financial Metrics Module is one of the main component of the CEO Dashboard web application. It is used to empower the admin with insights to the financial performance of the company. This module focuses on presenting key financial data, metrics, and analytical data for decision-making. This module displays data's like,
- Gross Profit
- OPEX to Profit Ratio
- NET Profit
- OPEX Ration per Month
- Forecasting for the Following Year
- Income Statement for the Previous Month [November]


---

## 5. Sales and Marketing Module
The Sales and Marketing Module is used to give an insights into the company's sales and marketing performance. This module is designed to provide a comprehensive overview of sales-related data and analytics, enabling the CEO to monitor, analyze, and optimize sales strategies effectively. This module is built using functionalities like.
- New Customers per Day
- Sales Revenue per Day
- Sales Profit per Day
- Monthly sales growth
- Sales target
- Amount spent on ADs
- Cost Per Thousand
- Cost per Click
- Click Through Rate


---

## 6. Operational Metrics Module
This module focuses on presenting key metrics related to production, inventory, and supply chain management, enabling the CEO to optimize operational efficiency. This module displays details of the employees like,
- Number of Employees per Department
- Average Salary per Department
- Salary Range Breakdown
- Contribution per department
- Employee gender breakdown


---

## 7. Collaboration and Communication Modulle
The Collaboration and Communication Module facilitates seamless interaction and information exchange between the CEO and other team members. It also allows the Admin to share documents. Feature of this module.
- Real-Time Chat Storage and Retrieval
- Choose the Employee to Chat with
- Email Integration
- Document Sharing
- Document Preview


## Languages and Tools Used
<section class="Front-End Tools" style = "display: flex; flex-direction: row; gap: 5em;">
    <div style = "display: flex; flex-direction: column; align-items: center;">
        <h3>Languages</h3>
        <div style = "display: flex; flex-direction:row; gap:1em">
            <img src="https://cdn-icons-png.flaticon.com/128/1051/1051277.png" style = "Width: 50px; height:50px">
            <img src="https://cdn-icons-png.flaticon.com/128/732/732190.png" style = "Width: 50px; height:50px">
            <img src="https://cdn-icons-png.flaticon.com/128/1199/1199124.png" style = "Width: 50px; height:50px">
            <img src="https://cdn-icons-png.flaticon.com/128/5968/5968350.png" style = "Width: 50px; height:50px">
            <img src="https://cdn-icons-png.flaticon.com/128/1199/1199128.png" style = "Width: 50px; height:50px">
            <!-- <img src="https://cdn.iconscout.com/icon/premium/png-512-thumb/markdown-2752127-2284944.png?f=webp&w=512" style = "Width: 50px; height:50px"> -->
        </div>
    </div>
    <div style = "display: flex; flex-direction: column; align-items: center;">
        <h3>Tools Used</h3>
        <div style = "display: flex; flex-direction:row; gap:1em">
            <img src="https://img.icons8.com/?size=96&id=9OGIyU8hrxW5&format=png" style = "Width: 50px; height:50px">
            <img src="https://cdn-icons-png.flaticon.com/128/5968/5968313.png" style = "Width: 50px; height:50px">
            <!-- <img src="https://cdn-icons-png.flaticon.com/128/11518/11518876.png" style = "Width: 50px; height:50px"> -->
            <img src="https://cdn-icons-png.flaticon.com/128/3291/3291695.png" style = "Width: 50px; height:50px">
        </div>
    </div>
</section>

## Getting Started on your device
To get started, you'll need a few things installed in order to run this project locally. Please follow these instructions carefully!

### TO install all required pip packages
```
pip install -r requirements.txt
```

### To access local database, Modify the code in app.py
```
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your Password",
    database="DB Name"
)
```

### TO run the application either press f5-key or,
```
cd CEO-DASHBOARD
python app.py
```

### To preview output of the application
#### On server Device
```
http://127.0.0.1:5000/login
On the server system
```
#### On Client Device
```
http://server-IP:5000/login
( Connect to the servers network either using hotspot or wi-fi and enter the IP-address of the server device along with the port:5000/login )
```

---
---

## File Structure
```
CEO-Dashboard-Blueprint
|
|----- authentication
|       |----- static
|       |       |----- css
|       |       |       |----- login.css
|       |       |       |----- signup.css
|       |       |----- images
|       |----- templates
|       |       |----- login.html
|       |       |----- otpValidation.html
|       |       |----- signup.html
|       |       |----- verifyEmail.html
|       |----- authentication.py
|
|----- communicationPage
|       |----- static
|       |       |----- javascript
|       |       |       |----- chat_module.js
|       |       |----- uploads
|       |       |----- chat_module.css
|       |----- templates
|       |       |----- communicationPage.html
|       |----- chat_history.json
|       |----- communicationPage.py
|       |----- document_history.json
|
|----- financialPage
|       |----- static
|       |       |----- javascript
|       |       |       |----- financial_module.js
|       |       |----- financial_moduel.css
|       |----- templates
|       |       |----- financialPage.html
|       |----- financialPage.py
|
|----- landingPage
|       |----- static
|       |       |----- javascript
|       |       |       |----- landing_module.js
|       |       |----- landing_moduel.css
|       |----- templates
|       |       |----- landingPage.html
|       |----- landingPage.py
|
|----- marketingPage
|       |----- static
|       |       |----- javascript
|       |       |       |----- marketing_module.js
|       |       |----- marketing_moduel.css
|       |----- templates
|       |       |----- marketingPage.html
|       |----- marketingPage.py
|
|----- operationalPage
|       |----- static
|       |       |----- javascript
|       |       |       |----- operational_module.js
|       |       |----- operational_moduel.css
|       |----- templates
|       |       |----- operationalPage.html
|       |----- operationalPage.py
|
|----- app.py
|
|----- static
|       |----- navBar.css
|
|----- README.md
|----- Mark_down_sources
|----- notes.txt
|----- CEO dashboard.pdf

```

---
---