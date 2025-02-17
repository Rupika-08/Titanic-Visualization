import matplotlib.pyplot as plt
#Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40 , 50]
#create a scatter plot
plt.scatter(x,y, color='red', label='Scatter Plot')
#add labels and tittle
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Scatter Plot')
#add a legend
plt.legend()
#display the plot
plt.show()