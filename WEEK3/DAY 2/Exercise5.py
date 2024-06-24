#Create a class called TheIncredibles. This class should inherit from the Family class:
#This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
#Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
#Add a method called incredible_presentation which :
#Print a sentence like “*Here is our powerful family **”
#Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
#Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
#    [
#        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#    ]
#Call the incredible_presentation method.
#Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
#Call the incredible_presentation method again.

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the new addition!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(member)


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} uses power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")

    def incredible_presentation(self):
        print(f"Here is our powerful family {self.last_name}")
        super().family_presentation()

members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_family = TheIncredibles("Incredibles", members)

incredibles_family.incredible_presentation()

incredibles_family.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

incredibles_family.incredible_presentation()

try:
    incredibles_family.use_power('Michael') 
    incredibles_family.use_power('Baby Jack')  
except Exception as e:
    print(e)
