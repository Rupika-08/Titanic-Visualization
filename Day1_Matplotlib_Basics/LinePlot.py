import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y, marker='o', color='blue', label='Line Plot')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Add a legend
plt.legend()

# Display the plot
plt.show()