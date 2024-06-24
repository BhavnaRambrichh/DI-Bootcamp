#Create a class called Dog.
#In this class, create an __init__ method that takes two parameters :
# name and height. This function instantiates two attributes, which values are the parameters.
#Create a method called bark that prints the following string “<dog_name> goes woof!”.
#Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
#Print the details of his dog (ie. name and height) and call the methods bark and jump.
#Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
#Print the details of her dog (ie. name and height) and call the methods bark and jump.
#Create an if statement outside of the class to check which dog is bigger. 
# Print the name of the bigger dog.

class Dog():
    
    def __init__(self,name,height):
        self.name = name
        self.height = height 
        self.x = height*2  
        
    def bark(self):
        print(f"{self.name} goes woof !")
        
    def jump(self):
        print(f"{self.name} jumps {self.x}cm high")
        
dog = Dog("Beau",40)  
dog.bark()
dog.jump()

davids_dog =Dog("Rex",50)

print(f"David's dog name: {davids_dog.name}")
print(f"David's dog height: {davids_dog.height} cm")

davids_dog.bark()
davids_dog.jump()

sarahs_dog=Dog("Teacup",20)
print(f"Sarah's dog name: {sarahs_dog.name}")
print(f"Sarah's dog height: {sarahs_dog.height} cm")

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")
