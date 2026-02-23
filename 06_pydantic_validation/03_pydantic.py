# data validation offered by pydantic
from pydantic import EmailStr , BaseModel , AnyUrl , Field
from typing import Optional , Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=40,title="name of patient",description="enter patient name only 40 characters are allowed ",examples=['Ani','kapoor'])]
    email : Optional[EmailStr] = None
    Linkedin_url : Optional[AnyUrl] = None
    married : Annotated[bool,Field(default=False ,description="is marreid or not")]
    age : Annotated[int , Field(strict=True,gt=10,le=100)]
  
# add Patient to DB 
def add_patient(patient : Patient):
    print(patient.name)
    print(patient.email)
    
info={
    'name' : 'anirudh' ,
    'email' : 'anirudh@gmail.com',
   #  'Linkedin_url' :'abc' 
    'age' : 11
} 

patient1=Patient(**info)

add_patient(patient1)
    