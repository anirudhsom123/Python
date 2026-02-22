from pydantic import BaseModel
from typing import List , Dict , Optional

# type validation
class Patient(BaseModel):
    name:str
    age:int
    married : bool
    weight:Optional[float] = None # if we want to make a optional entry for user then we can use Optional provided by typing module

    allergies:Optional[List[str]]=None # why not used list because list only validate   list but we want to validate the values inserted in list as well i.e is list contains value of string type or not

    contact_details:Dict[str,str] # if used dict it can only check is the value provided is dict or not but with Dict i can check for key,value pairs type as well.


# function to insert patient into DB
def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


# patient info
info={
    'name' : 'anirudh',
    'age' : 22 ,
    'married' :True ,
    # 'weight' : 70.00 ,
    'allergies' : ['pollen','dust'],
    'contact_details' : {
        'email' : 'abc@gmail.com' ,
        'phone' : '123456'
    }

}

# pydantic object for info
patient1=Patient(**info)

# insert patient into DB
insert_patient(patient1)
