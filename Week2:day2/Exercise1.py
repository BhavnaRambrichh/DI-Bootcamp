#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {2,4,5,6}
my_fav_numbers.add(8)
my_fav_numbers.add(10)
my_fav_numbers.remove(10)

print (my_fav_numbers)

friend_fav_numbers = {11,14,16,20}

our_fav_numbers =my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)
