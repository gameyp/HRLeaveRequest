from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user(Base):
    __tablename__ = 'users'

    userID = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)
    employeeID = Column(String)

    def __init__(self, userID, username, password, role, employeeID):
        self.userID = userID
        self.username = username
        self.password = password
        self.role = role
        self.employeeID = employeeID

    
    def to_dict(self):
        return {
            'userID': self.userID,
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'employeeID': self.employeeID,
        }

