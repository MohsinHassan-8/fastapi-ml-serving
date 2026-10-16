from pydantic import BaseModel

class Address(BaseModel):
       city : str
       state : str
       pin : str

class Patient(BaseModel):
       name : str
       gender : str = 'Male'
       address : Address

address_dict = {'city' : 'lhr' , 'state': 'punjab', 'pin' : 'P001'}
address_1 = Address(**address_dict)

patient_dict = {'name' : 'Mohsin', 'address' : address_1}
patient_1 = Patient(**patient_dict)

temp = patient_1.model_dump()
print(temp)
print(type(temp))

temp_1 = patient_1.model_dump_json()
print(temp_1)
print(type(temp_1))

temp_2 = patient_1.model_dump(include=['name' , 'gender'])
print(temp_2)

temp_3 = patient_1.model_dump(include={'address' : ['city']})
print(temp_3)

temp_4 = patient_1.model_dump(exclude_unset=True)
print(temp_4)
