from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from controllers.employeeController import employeeController
from controllers.userController import userController
from controllers.requestController import requestController

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
        return redirect(url_for('dashboardLeaveRequest'))
    
@app.route('/dashboard')
def dashboard():
    user = {'firstname': 'Test', 'lastname': 'User'}
    employees = employeeController.get_employees()
    return render_template('dashboardPage.html', user=user, employees=employees)

@app.route('/dashboardLeaveRequest')
def dashboardLeaveRequest():
    employeerequests = requestController.get_request_and_employee_data()

    return render_template('dashboardLeaveRequestPage.html', lstrequests=employeerequests)

@app.route('/requestPage')
def request_page():
    return render_template('requestPage.html')

# @app.route('/editRequestPage')
# def editRequestByRequestId():
#     # Get the query parameters from the request
#     qstr_requestid = request.args.get('requestID')
#     employeerequest = requestController.get_request_and_employee_data_by_requestid(qstr_requestid)

#     return render_template('editRequestPage.html', request=employeerequest)

# @app.route('/updateRequest', methods=['POST'])
# def updateRequest():
#     requestId = request.form.get('requestId')
#     startDate = request.form.get('password')
#     endDate = request.form.get('username')
#     leaveType = request.form.get('leaveType')

#     requestController.update_request_by_requestid(requestId, startDate, endDate, leaveType)
    
# @app.route('/deleteRequest', methods=['POST'])
# def deleteRequest():
#     requestId = request.form.get('requestId')
#     requestController.delete_request_by_requestid(requestId)

@app.route('/addRequest', methods=['POST'])
def addRequest():
    startDate = request.form.get('startDate')
    endDate = request.form.get('endDate')
    leaveType = request.form.get('leaveType')
    requestReason = request.form.get('requestReason')
    employeeID = request.form.get('employeeID')

    requestController.create_request(employee_id=employeeID, start_date=startDate, end_date=endDate, leaveType=leaveType, reason= requestReason , status='Approved')
    return redirect(url_for('dashboardLeaveRequest'))

if __name__ == '__main__':
    app.run(debug=True)
