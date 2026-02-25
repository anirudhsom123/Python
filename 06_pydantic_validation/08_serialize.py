# exporting model as python dictionary or json 
from pydantic import BaseModel


class Address(BaseModel):
    city : str
    state : str
    pincode : str


class Patient(BaseModel):
    name : str
    age : int
    address : Address

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
# patient1.model_dump(include=['name','address'])
# values that are not set by user will be excluded
patient1.model_dump(exclude_unset=True)
# exclude age and state from address
patient1.model_dump(exclude=['age',{'address' : ['state']}])


