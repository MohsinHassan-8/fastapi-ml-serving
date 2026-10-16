from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
       name : str
       age : int
       email : EmailStr
       weight : float 
       height : float
       married : bool 
       allergies : List[str] 
       contact_details : Dict[str , str]

       @computed_field
       @property
       def calc_bmi(self) -> float:
              bmi = round( self.weight / (self.height**2) , 2)
              return bmi
       



patient_info = {'name' : 'Mohsin', 'age' : 20, 'email': 'hehe@cui.edu', 'weight' : 75.5, 'height': 1.5, 'married':True, 'allergies':['hehe1', 'hehe2'], 'contact_details': {'number': '03094455'} }
patient_1 = Patient(**patient_info)

def insert_data(patient : Patient):
       print(patient.name)
       print(patient.age)
       print(patient.calc_bmi)
       print('Inserted')

insert_data(patient_1)

