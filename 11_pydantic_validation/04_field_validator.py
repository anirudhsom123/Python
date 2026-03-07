from pydantic import BaseModel , EmailStr , field_validator
from typing import Optional

# we want to validate if the email is from @hdfc or @axis OR not 
# we can do this using field validator 
class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    
    @field_validator('name')
    @classmethod
    def convert_name(cls,value):
        return value.upper()
    
    #before type conversion
    # will validate the value before type conversion hence the int value provided in string format will through ValueError
    @field_validator('age',mode='before')
    @classmethod
    def age_before_conversion(cls,value):
        if 0<value<=100:
            return value
        
        raise ValueError('age should be btwn 0 to 101')
    
    #after type conversion
    # validation happens after the type conversion hence will not through error for integer value provided in string format
    @field_validator('age',mode='after')
    @classmethod
    def age_before_conversion(cls,value):
        if 0<value<=100:
            return value
        
        raise ValueError('age should be btwn 0 to 101')
    
    @field_validator('email')
    @classmethod
    def validate_email(cls,value):
        
        domain=['hdfc.com','axic.com']
        
        suffix=value.split('@')[-1]
        
        if suffix not in domain:
            raise ValueError('not a valid user')
        
        return value
    
    
    

info ={
    'name' :'anirudh',
    'age' : 22 ,
    'email' :'abc@hdfc.com'  
}

patient1=Patient(**info)

# add patient to DB
def add_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    
add_patient(patient1)