#Modify the plots from Exercise 8 to include a legend. 
# Use the legend function from Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2, 1)
axs[0].plot(x,y1,color='tab:blue',label="blue line")
axs[0].legend(title="y = sin(x)", loc="upper right", shadow=True)


axs[1].scatter(x,y2,color='tab:blue',label="blue dot")
axs[1].legend(title="y = cos(x)", loc="upper left", shadow=True)


plt.show()