from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class employee(Base):
    __tablename__ = 'employees'

    employeeID = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    birthdate = Column(String)
    department = Column(String)

    def __init__(self, employeeID, firstname, lastname, birthdate, department):
        self.employeeID = employeeID
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.department = department

    def to_dict(self):
        return {
            'employeeID': self.employeeID,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birthdate': self.birthdate,
            'department': self.department,
        }
