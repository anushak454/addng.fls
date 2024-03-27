my_dict = {"name" : "Anusha", "place" : "ongole", "position" : "Trainee","company" : "Infinitude","Address" :"Hyderabad"}
print(my_dict)
new_dict1 = my_dict.pop("Address")
print("removed value:",new_dict1)
print(my_dict)
my_dict["car"] = "Tesla"
print(my_dict)
my_list = list(my_dict.items())
print(my_list)

"""
output::
{'name': 'Anusha', 'place': 'ongole', 'position': 'Trainee', 'company': 'Infinitude', 'Address': 'Hyderabad'}
removed value: Hyderabad
{'name': 'Anusha', 'place': 'ongole', 'position': 'Trainee', 'company': 'Infinitude'}
{'name': 'Anusha', 'place': 'ongole', 'position': 'Trainee', 'company': 'Infinitude', 'car': 'Tesla'}
[('name', 'Anusha'), ('place', 'ongole'), ('position', 'Trainee'), ('company', 'Infinitude'), ('car', 'Tesla')]

Process finished with exit code 0
"""
