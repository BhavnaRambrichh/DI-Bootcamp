#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Given the following object:

#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


#How much does each family member have to pay ?

#Print out the family’s total cost for the movies.
#Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names 
# and ages and add them into a family dictionary that is initially empty).

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name,age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    print(f"{name.capitalize()} has to pay ${ticket_price}.")
    total_cost += ticket_price

print(f"\nThe family's total cost for the movies is: ${total_cost}")

#Part B ==> Bonus
family = {}

print("Enter family members' names and ages (type 'done' to finish):")

while True:
    name = input("Enter the name of the family member (or 'done' to finish): ").strip()
    if name == 'done':
        break
    
    age = int(input(f"Enter the age of {name}: ").strip())
    family[name] = age

total_cost = 0

print("\nTicket costs for the entered family members:")
for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    print(f"{name.capitalize()} has to pay ${ticket_price}.")
    total_cost += ticket_price

print(f"\nThe family's total cost for the movies is: ${total_cost}")