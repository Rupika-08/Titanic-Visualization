import seaborn as sns
import matplotlib.pyplot as plt
#Load titanic dataset
titanic = sns.load_dataset('titanic')
#Display the first few rows
print(titanic.head())
# Bar plot for average age by passenger class
sns.barplot(x='class', y='age', data=titanic, palette='magma', ci=None)

# Add labels and title
plt.xlabel('Passenger Class')
plt.ylabel('Average Age')
plt.title('Average Age by Passenger Class')

# Display the plot
plt.show()