from flask import Flask
from authentication.authentication import auth, init_mysql_auth

app = Flask(__name__)
app.secret_key = 'r$W9#kLp2&QnX@5*8yZ$'

init_mysql_auth(app)
app.register_blueprint(auth)

if __name__ == "__main__":
    [app.run(host="0.0.0.0", port=5000, debug=True)]