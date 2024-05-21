#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Ask a family the age of each person who wants a ticket.

#Store the total cost of all the family’s tickets and print it out.

#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#At the end, print the final list.

total_cost = 0

while True:
    age = input("Enter the age of the family member (or 'done' to finish): ")
    if age == 'done':
        break
    age = int(age)
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price

print(f"Total cost of all the family's tickets is: Rs.{total_cost}")


teenagers = ["Kelsi", "Troy", "Gabriella", "Ryan", "Chad","Taylor","Sharpay"]

allowed_teenagers = []

for teenager in teenagers:
    age = int(input(f"Enter the age of {teenager}: "))
    if 16 <= age <= 21:
        print(f"{teenager} is not permitted to watch the movie.")
    else:
        allowed_teenagers.append(teenager)

print("Final list of teenagers allowed to watch the movie:")
print(allowed_teenagers)