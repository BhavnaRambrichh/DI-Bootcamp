#Instantiate three Cat objects using the code provided above.
#Outside of the class, create a function that finds the oldest cat and returns the cat.
#Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
    def __str__(self) -> str:
        return self.name
        
Cat_1 = Cat("Garfield",3)
Cat_2 = Cat("Luna",8)
Cat_3 = Cat("Kitty",10) 

def find_oldestcat(Cats):
    
    oldest_cat = Cat[0]
    for cat in Cats:
      if cat.age > oldest_cat.age:
       oldest_cat = cat
    return oldest_cat 
       
Cat = [Cat_1, Cat_2, Cat_3]
oldest_cat = find_oldestcat(Cat)       
   
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age}years old.")    

