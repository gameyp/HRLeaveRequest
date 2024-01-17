from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.employee import employee
from models.user import user

class userController:
    
        def get_users():
            engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
            Session = sessionmaker(bind=engine)
            session = Session()
    
            users = session.query(user).all()
            return users
        
        def get_user_by_id(id):
            engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
            Session = sessionmaker(bind=engine)
            session = Session()
    
            us = session.query(user).filter_by(id=id).first()
            return us
    
        def get_user_by_username(username):
            engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
            Session = sessionmaker(bind=engine)
            session = Session()
    
            user = session.query(user).filter_by(username=username).first()
            return user 
    
        def get_user_by_username_and_password(username, password):
            engine = create_engine('sqlite:///HRLeaveRequest.db', echo=True)
            Session = sessionmaker(bind=engine)
            session = Session()
    
            users = session.query(user).filter_by(username=username, password=password).first()
            return users  