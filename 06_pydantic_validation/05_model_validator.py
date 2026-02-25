from pydantic import BaseModel , model_validator
from typing import Dict

class Patient(BaseModel):
    name : str
    age : int
    contact : Dict[str,str]
    
    @model_validator(mode='after')
    def validate_contact(self):
        if self.age >60 and 'emergency' not in self.contact:
            raise ValueError("patient greater then 60 should have a emergency number")
        return self
    

#add patient to DB
def add_patient(patient : Patient):
    print(patient.name)

info={
    'name' : 'anirudh',
    'age' : 61 ,
    'contact' : {
        'number' : '11111111',
        'emergency' : '22222222'
    }
}

patient1=Patient(**info)

add_patient(patient1)