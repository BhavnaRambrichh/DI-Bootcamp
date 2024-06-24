#Modify the scatter plot from Exercise 3 to include a title (“Children’s Height vs Age”), 
# and labels for the x-axis (“Age (years)”) and y-axis (“Height (cm)”).

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5] 
y = [75, 80, 88, 95, 105]


fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set(title="Children's Height vs Age", xlabel="Age (years)", ylabel="Height(cm)")
fig.savefig('my_figureEx5.png')

plt.show()

#EXERCISE 6#Save both plots (from exercises 4 and 5) to your local machine as .png files. Use the savefig function from Matplotlib.
# Answer: It is saved in the folder Pictures <==