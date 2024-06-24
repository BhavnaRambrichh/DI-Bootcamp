#Create a class called Dog with the following attributes name, age, weight.
#Implement the following methods in the Dog class:
#bark: returns a string which states: “<dog_name> is barking”.
#run_speed: returns the dogs running speed (weight/age*10).
#fight : takes a parameter which value is another Dog instance, called other_dog. 
# This method returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.
# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight =weight
    def bark(self):
        return f"{self.name} is barking"     
    def run_speed(self):
        return (self.weight/self.age)*10
    
    def fight(self,other_dog):
        self_score = self.run_speed() * self.weight 
        other_score = other_dog.run_speed() * other_dog.weight
        
        if self_score > other_score:
            return f"{self.name} wins the fight"
        elif self_score < other_score:
            return f"{other_dog.name} wins the fight"
        else:
            return "It's a tie!"
        
dog1 = Dog("Beau", 3, 20)
dog2 = Dog("Grand", 4, 25)
dog3 = Dog("Omy", 6, 18)

print(dog1.bark())  
print(dog2.bark())  
print(dog3.bark())  

print(dog1.run_speed()) 
print(dog2.run_speed())  
print(dog3.run_speed())  


print(dog1.fight(dog2))  
print(dog2.fight(dog3))
print(dog1.fight(dog3))  
