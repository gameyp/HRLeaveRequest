from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class request(Base):
    __tablename__ = 'requests'

    requestID = Column(Integer, Sequence('request_id_seq'), primary_key=True)
    requestDate = Column(DateTime, default=datetime.utcnow)
    requestReason = Column(String)
    requestStatus = Column(String)
    leaveType = Column(String)
    startLeaveDate = Column(String)
    endLeaveDate = Column(String)
    employeeID = Column(String)

    def __init__(self, startLeaveDate, endLeaveDate, leaveType, requestReason, requestStatus, employeeID):
        self.startLeaveDate = startLeaveDate
        self.endLeaveDate = endLeaveDate
        self.leaveType = leaveType
        self.requestReason = requestReason
        self.requestStatus = requestStatus
        self.employeeID = employeeID

    def to_dict(self):
        return {
            'requestID': self.requestID,
            'requestDate': self.requestDate,
            'requestReason': self.requestReason,
            'requestStatus': self.requestStatus,
            'leaveType': self.leaveType,
            'startLeaveDate': self.startLeaveDate,
            'endLeaveDate': self.endLeaveDate,
            'employeeID': self.employeeID,
        }
