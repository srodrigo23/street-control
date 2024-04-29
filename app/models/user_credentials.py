
from app.extensions import db
from app.models.base import Base

class UserCredentials(Base):
  __tablename__ = "UserCredentials"
 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
  username = db.Column(db.String())
  password = db.Column(db.String())
  person_id = db.Column(db.Integer, db.ForeignKey('Persons.id'), nullable=False)



  def __init__(self, username:str, password:str):
    self.username = username
    self.password = password

  
  # def __repr__(self):
  #     return f"{self.first_name} {self.last_name} : {self.id} : {self.date_created}"