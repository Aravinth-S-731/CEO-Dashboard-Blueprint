from flask import Flask, session, redirect, url_for
from datetime import timedelta


from authentication.authentication import auth, init_mysql_auth
from landingPage.landingPage import landingPage

app = Flask(__name__)
app.secret_key = 'r$W9#kLp2&QnX@5*8yZ$'

init_mysql_auth(app)

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect (url_for('auth.login'))

app.register_blueprint(auth)
app.register_blueprint(landingPage)

if __name__ == "__main__":
    [app.run(host="0.0.0.0", port=5000, debug=True)]