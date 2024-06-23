#Modify the line plot from Exercise 2 to include a title (“Product Demand vs Price”),
# and labels for the x-axis (“Price”) and y-axis (“Demand”).

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5] 
y = [75, 80, 88, 95, 105]


fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set(title='Product Demand vs Price', xlabel='Price', ylabel='Demand')
fig.savefig('my_figure.png')

plt.show()

#Save both plots (from exercises 4 and 5) to your local machine as .png files. Use the savefig function from Matplotlib.
