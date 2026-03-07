from pydantic import BaseModel


class Address(BaseModel):
    city : str
    state : str
    pincode : str


class Patient(BaseModel):
    name : str
    age : int
    address : Address



# patient to DB
def add_patient(patient: Patient):
    print(patient.name)
    print(patient.address)
    
add_dict={
    'city' :'meerut',
    'state' : 'up',
    'pincode' : '250002'
}
address1=Address(**add_dict)

info={
    'name' : 'anirudh',
    'age' : 22,
    'address' : address1
}

patient1=Patient(**info)

add_patient(patient1)

