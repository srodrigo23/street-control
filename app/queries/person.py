
from app.models.person import Person

def get_all_persons()->list:
    return Person.query.all()

def insert_user(person: Person)->bool:
    Person.insert(person)
    return True