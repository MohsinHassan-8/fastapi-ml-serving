from pydantic import BaseModel

class Address(BaseModel):
       city : str
       state : str
       pin : str

class Patient(BaseModel):
       name : str
       gender : str
       address : Address

address_dict = {'city' : 'lhr' , 'state': 'punjab', 'pin' : 'P001'}
address_1 = Address(**address_dict)

patient_dict = {'name' : 'Mohsin', 'gender' : 'male', 'address' : address_1}
patient_1 = Patient(**patient_dict)

print(patient_1.name)
print(patient_1.address.city)
