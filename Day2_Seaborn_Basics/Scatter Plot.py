import seaborn as sns
import matplotlib.pyplot as plt
#Load titanic dataset
titanic = sns.load_dataset('titanic')
#Display the rows
print(titanic.head())
sns.scatterplot(x='age', y='fare', data=titanic, hue='class', palette='coolwarm')
#Add labels and title
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs Fare by Passenger Class')
#Display the plot
plt.show()