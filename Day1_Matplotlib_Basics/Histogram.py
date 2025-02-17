import matplotlib.pyplot as plt
# Data
data = [1, 2, 2, 3, 3, 4 , 4, 4, 5, 5, 5, 5, 5]
# Create a histogram
plt.hist(data, bins=5, color='yellow', edgecolor='black')
# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Sample Histogram')
# Display the plot
plt.show()