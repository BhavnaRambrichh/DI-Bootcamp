#Write code that asks the user for a number and determines whether this number is odd or even.

#number = input("enter a number")

number =int(input("enter a number"))


if (number % 3) == 0:
   print(number,"is even")
else:
   print(number,"is odd")
