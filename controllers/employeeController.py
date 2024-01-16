from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.employee import employee

class employeeController:

    def get_employees():
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        
        employees = session.query(employee).all()
        return employees
    
    def get_employee_by_id(id):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        employee = session.query(employee).filter_by(id=id).first()
        return employee

    def get_employee_by_firstname(firstname):
        engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        employees = session.query(employee).filter_by(firstname=firstname).first()
        return employees  

