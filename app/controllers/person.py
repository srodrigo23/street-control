from app.queries import person

def get_all_users()->list:
  return person.get_all_persons()

# first_name:str, second_name:str, last_name:str, cellphone:str, email:str
def add_new_person(first_name:str, second_name:str, last_name:str, cell_phone:str, email:str)->bool:
  from app.models.person import Person
  new_person = Person(
    first_name=first_name,
    second_name=second_name,
    last_name=last_name,
    cell_phone=cell_phone,
    email=email
  )
  return person.insert_user(user=new_person)