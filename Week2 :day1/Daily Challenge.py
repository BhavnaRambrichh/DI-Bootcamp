#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

#Then, print the first and last characters of the given text.

#Using a for loop, construct the string character by character: Print the first character, then the second, 
# then the third, until the full string is printed.

user_string = input("Enter a string that must be 10 characters long:")

if len(user_string) < (10):
  print ("string not long enough") 
 
elif len(user_string) > 10:
  print("string too long")    
 
else: 
    print("perfect string")
    
    
if len(user_string) == 10:
    
     first_char = user_string[0]
     last_char = user_string[-1]
     print(first_char[0])
     print(last_char[-1])
     
for x in range (0,len(user_string)):
    