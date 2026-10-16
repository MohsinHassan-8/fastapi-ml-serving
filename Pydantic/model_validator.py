from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
       name : str
       age : int
       email : EmailStr
       weight : float 
       married : bool 
       allergies : List[str] 
       contact_details : Dict[str , str]

       @model_validator(mode= 'after')
       @classmethod
       def age_contact(cls, model):
              if model.age > 60 and 'emergency' not in model.contact_details:
                     raise ValueError('Patient should have some emergency contact')
              return model



patient_info = {'name' : 'Mohsin', 'age' : 20, 'email': 'hehe@cui.edu', 'weight' : 75.5, 'married':True, 'allergies':['hehe1', 'hehe2'], 'contact_details': {'number': '03094455'} }
patient_1 = Patient(**patient_info)

def insert_data(patient : Patient):
       print(patient.name)
       print(patient.age)
       print('Inserted')

insert_data(patient_1)

