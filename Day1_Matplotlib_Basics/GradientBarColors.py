import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct']
sales = [250, 300, 450, 600, 700]

# Create a gradient color map
# Create a gradient color map
colors = plt.cm.Blues(np.linspace(0.5, 1, len(months)))

# Plotting Bar Chart with customizations
plt.bar(months, sales, color='black', edgecolor='black', width=0.6, label='Monthly Sales')

# Add labels and title
plt.xlabel('Months', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Monthly Sales Bar Chart with Gradient Colors', fontsize=15)

# Add gridlines
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
#axis='y': Adds gridlines only for the y-axis.
#linestyle='--': Uses dashed gridlines.
#alpha=0.7: Makes the gridlines slightly transparent.


# Add legend
plt.legend()

# Display the plot
plt.show()
