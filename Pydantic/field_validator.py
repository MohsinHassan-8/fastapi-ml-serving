from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
       name : str
       age : int
       email : EmailStr
       weight : float 
       married : bool 
       allergies : List[str] 
       contact_details : Dict[str , str]

       @field_validator('email')
       @classmethod
       def email_method(cls, value):
              valid_domains = ['cui.edu','ucp.edu']
              domain_name = value.split('@')[-1]
              if domain_name not in valid_domains:
                     raise ValueError('Not a valid domain')
              return value
       @field_validator('name')
       @classmethod
       def name_upper(cls, value):
              return value.upper()
       
       @field_validator('age', mode = 'before')
       @classmethod
       def age_val(cls, value):
              if 0 < value < 60:
                     return value
              else:
                     raise ValueError('Invalid Age')


patient_info = {'name' : 'Mohsin', 'age' : 20, 'email': 'hehe@cui.edu', 'weight' : 75.5, 'married':True, 'allergies':['hehe1', 'hehe2'], 'contact_details': {'number': '03094455'} }
patient_1 = Patient(**patient_info)

def insert_data(patient : Patient):
       print(patient.name)
       print(patient.age)
       print('Inserted')

insert_data(patient_1)

