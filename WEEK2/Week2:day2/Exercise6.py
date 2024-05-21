#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
   
my_name = "Bhavna" 
 
while True: 
    user_name = input("Please enter your name : ")
    if user_name == my_name:
        break
    else:
        print("Enter correct name!: ")
