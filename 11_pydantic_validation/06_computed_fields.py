# field that is needed to be calculated on the basis of input fields
# eg. if user gives weight and height we can compute BMI for user

from pydantic import BaseModel , computed_field


class Patient(BaseModel):
    name : str
    height : float
    weight : float 
    
    @computed_field()
    @property
    def bmi(self)->float:
        bmi=self.weight/(self.height**2)
        return bmi
        
    

# add patient to DB
def add_patient(patient: Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
     
    
info ={
    'name' : 'anirudh',
    'height' :1.92 ,
    'weight' : 70
}

patient1=Patient(**info)

add_patient(patient1)