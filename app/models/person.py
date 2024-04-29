
from app.extensions import db
from app.models.base import Base

class Person(Base):
    __tablename__ = "Persons"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = db.Column(db.String(), nullable=False)
    second_name = db.Column(db.String())
    first_last_name = db.Column(db.String(), nullable=False)
    second_last_name = db.Column(db.String())

    cellphone = db.Column(db.String(12))
    email = db.Column(db.String(30))
    is_user = db.Column(db.Boolean, default=False)
    credentials = db.relationship('UserCredentials', backref='Persons', lazy=True)

    def __init__(
        self, first_name:str, second_name:str, 
        first_last_name:str, second_last_name:str, 
        cellphone:str, email:str, is_user:bool) -> None:

        self.first_name = first_name
        self.second_name = second_name
        self.first_last_name = first_last_name
        self.second_last_name = second_last_name
        self.cellphone = cellphone
        self.email = email
        self.is_user = is_user
        # self. = 
 
    def __repr__(self):
        return f"""{self.first_name} {self.last_name} : {self.id} : {self.date_created}"""