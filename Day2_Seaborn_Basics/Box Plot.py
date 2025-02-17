import seaborn as sns
import matplotlib.pyplot as plt
#Load titanic data
titanic=sns.load_dataset('titanic')
#Display the rows
print(titanic.head())
#boxplot for 'age' by 'class'
sns.boxplot(x='class', y='age', data=titanic, palette='Set2')
#Add labels and title
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.title('Age Distribution by Passenger Class')
#Display the plot
plt.show()