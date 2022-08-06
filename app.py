from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')

def login_main():
    return render_template("auth-login-basic.html")

@app.route('/auth-forgot-password-basic.html')
def forgot_password():
    return render_template("auth-forgot-password-basic.html")

@app.route('/pages-account-settings-notifications.html')
def settings_notifications():
    return render_template("pages-account-settings-notifications.html")

@app.route('/pages-account-settings-account.html')
def settings_account():
    return render_template("pages-account-settings-account.html")

@app.route('/pages-account-settings-connections.html')
def settings_connections():
    return render_template("pages-account-settings-connections.html")

@app.route('/index.html', methods=['POST'])
def dashboard():
    return render_template("index.html")

@app.route('/auth-login-basic.html')
def login_basic():
    return render_template("auth-login-basic.html")

@app.route('/auth-register-basic.html')
def register_basic():
    return render_template("auth-register-basic.html")

if __name__ == '__main__':
    app.run(debug=True)