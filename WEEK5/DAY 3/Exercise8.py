#Plot the line plot and scatter plot from Exercise 7 on the same figure using subplots. 
# Use plt.subplots to create a figure with two subplots.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2, 1)
axs[0].plot(x,y1,color='tab:blue')


axs[1].scatter(x,y2,color='tab:blue')

plt.show()