#Create a new python file and import your Dog class from the previous exercise.
#In the new python file, create a class named PetDog that inherits from Dog.
#Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
#Add the following methods:
#train: prints the output of bark and switches the trained boolean to True

#play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

#do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#“dog_name does a barrel roll”.
#“dog_name stands on his back legs”.
#“dog_name shakes your hand”.
#“dog_name plays dead”.

from Exercise2 import Dog  # Make sure dog.py is in the same directory as pet_dog.py
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(dog.name for dog in args)
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")


if __name__ == "__main__":
    pet_dog1 = PetDog("Teddy", 5, 30)
    pet_dog2 = PetDog("Fluffy", 3, 10)
    pet_dog3 = PetDog("Snoopy", 4, 18)

    
    pet_dog1.train()

    
    pet_dog1.play(pet_dog2, pet_dog3)

    pet_dog1.do_a_trick()
    pet_dog2.do_a_trick() 
