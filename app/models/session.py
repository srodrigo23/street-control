
from app.extensions import db
from app.models.base import Base

class Session(Base):
    __tablename__ = "Sessions"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # user_id = db.Column(db.Integer(), unique = True)
    # first_name = db.Column(db.String())
    # second_name = db.Column(db.String())
    # last_name = db.Column(db.String())
    # cellphone = db.Column(db.String(12))
    # email = db.Column(db.String(30))
    # home = db.Column(db.String(20))
    # registered_by = db.Column(db.String())

    def __init__(self, first_name:str, second_name:str, last_name:str, cellphone:str, email:str):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.cellphone = cellphone
        self.email = email
 
    def __repr__(self):
        return f"""{self.first_name} {self.last_name} : {self.id} : {self.date_created}"""