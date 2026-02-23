# data validation offered by pydantic
from pydantic import EmailStr , BaseModel , AnyUrl
from typing import Optional

class Patient(BaseModel):
    name: str
    email : Optional[EmailStr] = None
    Linkedin_url : Optional[AnyUrl] = None
  
# add Patient to DB 
def add_patient(patient : Patient):
    print(patient.name)
    print(patient.email)
    
info={
    'name' : 'anirudh' ,
    'email' : 'anirudh@gmail.com'
} 

patient1=Patient(**info)

add_patient(patient1)
    