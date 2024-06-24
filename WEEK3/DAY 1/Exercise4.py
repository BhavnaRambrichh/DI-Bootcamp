#Create a class called Zoo.
#In this class create a method __init__ that takes one parameter: zoo_name.
#It instantiates two attributes: animals (an empty list) and 
# name (name of the zoo).
#Create a method called add_animal that takes one parameter new_animal. 
# This method adds the new_animal to the animals list as long as it isn’t already in the list.
#Create a method called get_animals that prints all the animals of the zoo.
#Create a method called sell_animal that takes one parameter animal_sold. 
# This method removes the animal from the list and of course the animal needs to exist in the list.
#Create a method called sort_animals that sorts the animals alphabetically and 
# groups them together based on their first letter.

class Zoo():
    def __init__(self,zoo_name):
        self.animals =[]
        self.name = zoo_name 
        
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            
    def get_animals(self):
     print("All animals:")
     for animal in self.animals:
      print(animal) 
      
    def sell_animals(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            
    def sort_animals(self):
     sorted_animals = sorted(self.animals)
     grouped_animals = {}
     for animal in sorted_animals:
      first_letter = animal[0].upper()
      if first_letter not in grouped_animals:
        grouped_animals[first_letter] = []
        grouped_animals[first_letter].append(animal)
        
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")  
            
            
zoo = Zoo("Jurassik Zoo")
zoo.add_animal("Giraffe")    
zoo.add_animal("Panda")
zoo.add_animal("Elephant")
zoo.add_animal("Sloth")
zoo.add_animal("Gorilla")        
              
zoo.get_animals()
zoo.sell_animals("Giraffe")
zoo.get_animals()
zoo.sort_animals()            
       