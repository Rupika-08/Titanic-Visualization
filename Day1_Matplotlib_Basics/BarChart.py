import matplotlib.pyplot as plt
#Defining the Data
categories = ['A', 'B', 'C', 'D']
values = [15, 25, 30, 20]
#creating a bar chart
plt.bar(categories, values, color='green')
#Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')
#Display the plot
plt.show()