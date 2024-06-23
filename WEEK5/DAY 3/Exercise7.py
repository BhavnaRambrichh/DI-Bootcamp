#Create a line plot and scatter plot representing your favorite mathematical functions. 
# Change the line color to tab:blue for the line plot and use a marker of your choice for the scatter plot.

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,y1,color='tab:blue')

ax.scatter(x,y2,color='tab:blue')

plt.show()