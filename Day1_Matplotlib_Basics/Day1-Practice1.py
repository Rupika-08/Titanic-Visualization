#import matplotlib
import matplotlib.pyplot as plt
# data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [200, 240, 300, 280, 350]
#customize figure size
plt.figure(figsize=(8,6))
#create a plot
plt.plot(months, sales, marker='D', markersize=8, linestyle='--', color='purple', label = 'Line Plot')
#add labels, customize fontsize
plt.xlabel('Months', fontsize=12)
plt.ylabel('Sales', fontsize=12 )
plt.title('Monthly Sales', fontsize=14)
#add legend
plt.legend()
#display plot
plt.show()