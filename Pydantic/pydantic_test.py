from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
       name : Annotated[ str , Field( max_length = 50, title = 'Name of patient', description= 'Enter the name of patient', examples= ['Mohsin', 'Hassan'])]
       age : int = Field(gt = 5, lt = 60)
       email : EmailStr
       url : AnyUrl
       weight : float = Field( gt = 0 , strict= True )
       married : bool = False # Default value
       allergies : Optional[List[str]] = Field(max_length = 5, default = None)
       contact_details : Dict[str , str]

patient_info = {'name' : 'Mohsin', 'age' : 20}
patient_1 = Patient(**patient_info)

def insert_data(patient : Patient):
       print(patient.name)
       print(patient.age)
       print('Inserted')

insert_data(patient_1)

