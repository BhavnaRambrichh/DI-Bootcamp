#Create a basic scatter plot using the following data, which represents children’s heights at different ages:
#x = [1, 2, 3, 4, 5]  # Age
#y = [75, 80, 88, 95, 105]  # Height in cm
#Plot the x and y lists using a scatter plot and display the plot.
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5] 
y = [75, 80, 88, 95, 105]


fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()
