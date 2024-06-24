#Plot a histogram using the following data, which represents the distribution of grades in a class:
#grades = [88, 90, 95, 92, 88, 90, 88, 85, 93, 92, 90, 87, 95, 90, 88]

import matplotlib.pyplot as plt


grades = [88, 90, 95, 92, 88, 90, 88, 85, 93, 92, 90, 87, 95, 90, 88]

plt.hist(grades, bins=10, edgecolor='black', alpha=0.7)

plt.title('Distribution of Grades in a Class')
plt.xlabel('Grades')
plt.ylabel('Frequency')


plt.show()
