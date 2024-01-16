from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from controllers.employeeController import employeeController
from controllers.userController import userController

app = Flask(__name__)

@app.route('/')
def loginPage():
    return render_template('loginPage.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    uuu = userController.get_user_by_username_and_password(username, password)
    if uuu is None:
        return 'Invalid username or password'
    else:
        return render_template('dashboardPage.html')

@app.route('/dashboardPage')
def dashboard():
    return 'This is dashboardPage'

# Uncomment the following routes if needed
# @app.route('/modifyPage')
# def page3():
#     return 'This is modifyPage'

# @app.route('/requestPage')
# def page4():
#     return 'This is requestPage'

if __name__ == '__main__':
    app.run(debug=True)
