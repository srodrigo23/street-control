
from app.extensions import db
from app.models.base import Base

class User(Base):
  __tablename__ = "Users"
 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String())
  password = db.Column(db.String())

  def __init__(self, username:str, password:str):
    self.username = username
    self.password = password
  
  # def __repr__(self):
  #     return f"{self.first_name} {self.last_name} : {self.id} : {self.date_created}"