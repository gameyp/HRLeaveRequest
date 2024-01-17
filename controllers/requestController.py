from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.employee import employee
from models.request import request

class requestController:

    def get_request_and_employee_data():
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        employeereqeuests = session.query(request, employee).join(employee, request.employeeID == employee.employeeID).all()
        return employeereqeuests

    def get_requests():
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        requests = session.query(request).all()
        return requests
    
    def get_request_by_id(id):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        request = session.query(request).filter_by(id=id).first()
        return request
    
    def get_request_by_employee_id(employee_id):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        request = session.query(request).filter_by(employee_id=employee_id).first()
        return request
    
    def get_request_by_status(status):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        request = session.query(request).filter_by(status=status).all()
        return request
    
    def update_request(id, status):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        request = session.query(request).filter_by(id=id).first()
        request.status = status
        session.commit()
        return request
    
    def delete_request(id):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        request = session.query(request).filter_by(id=id).first()
        session.delete(request)
        session.commit()
        return request
    
    def create_request(employee_id, start_date, end_date, leaveType, reason, status):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

# request = R÷equest('1', '2022-01-01', 'Vacation', 'Pending', 'Annual', '2022-02-01', '2022-02-07', '123')
        new_request = request(requestReason=reason, startLeaveDate=start_date, endLeaveDate=end_date, leaveType=leaveType, employeeID=employee_id,requestStatus=status)
        session.add(new_request)
        session.commit()
        return new_request
    