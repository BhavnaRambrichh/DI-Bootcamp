#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#Remove “Banana” from the list.
#Remove “Blueberries” from the list.
#Add “Kiwi” to the end of the list.
#Add “Apples” to the beginning of the list.
#Count how many apples are in the basket.
#Empty the basket.
#Print(basket)

Basket = ["Banana","Apples","Oranges","Blueberries"]
Basket.remove("Banana")
Basket.remove("Blueberries")
Basket.append("Kiwi")
Basket.insert(0,"Apples")

Basket.count("Apples")
Basket.clear()
print(Basket)



