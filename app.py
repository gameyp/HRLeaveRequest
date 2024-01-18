from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from controllers.employeeController import employeeController
from controllers.userController import userController
from controllers.requestController import requestController

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HRLeaveRequest.db'
db = SQLAlchemy(app)
app.secret_key = 'gamie'

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
    elif uuu.employee is None:
        return 'User does not have an associated employee'

    else:
        session['userinfo'] = {'firstname': uuu.employee.firstname, 'lastname': uuu.employee.lastname, 'username': uuu.user.username, 'employeeID': uuu.user.employeeID, 'role': uuu.user.role}
        return redirect(url_for('dashboardLeaveRequest'))
        # return redirect(url_for('dashboardLeaveRequest'))
    
@app.route('/dashboard')
def dashboard():
    user = {'firstname': 'Test', 'lastname': 'User'}
    employees = employeeController.get_employees()
    return render_template('dashboardPage.html', user=user, employees=employees)


@app.route('/dashboardLeaveRequest')
def dashboardLeaveRequest():
    if 'userinfo' in session:
        ddd = session['userinfo']
        aa = {'firstname': ddd['firstname'], 'lastname': ddd['lastname'], 'username': ddd['username'], 'employeeID': ddd['employeeID'], 'role': ddd['role']}
        employeerequests = requestController.get_request_and_employee_data()
        return render_template('dashboardLeaveRequestPage.html', lstrequests=employeerequests, user=aa)
    
    return redirect(url_for('login'))

@app.route('/requestPage')
def request_page():
    if 'userinfo' in session:
        return render_template('requestPage.html')
    
    return redirect(url_for('login'))

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
    if 'userinfo' in session:
        ddd = session['userinfo']
        

        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        leaveType = request.form.get('leaveType')
        requestReason = request.form.get('requestReason')
        employeeID = ddd['employeeID']

        requestController.create_request(employee_id=employeeID, start_date=startDate, end_date=endDate, leaveType=leaveType, reason= requestReason , status='Approved')
        return redirect(url_for('dashboardLeaveRequest'))
    
    
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
