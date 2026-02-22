from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)

info={
    'name':'anirudh',
    'age': 22
}
patient1=Patient(**info)

insert_patient(patient1)
