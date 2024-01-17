from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from controllers.employeeController import employeeController
from controllers.userController import userController

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HRLeaveRequest.db'
db = SQLAlchemy(app)

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
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    user = {'firstname': 'Test', 'lastname': 'User'}
    employees = employeeController.get_employees()
    return render_template('dashboardPage.html', user=user, employees=employees)

@app.route('/modifyPage')
def page3():
    return 'This is modifyPage'

@app.route('/requestPage')
def request_page():
    return render_template('requestPage.html')

if __name__ == '__main__':
    app.run(debug=True)
