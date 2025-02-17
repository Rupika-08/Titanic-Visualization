import seaborn as sns
import matplotlib.pyplot as plt
#Load titanic data
titanic=sns.load_dataset('titanic')

#Pair plot for relationships between age, fare, pclass
sns.pairplot(titanic[['age', 'fare', 'pclass']], hue='pclass', palette='Set1')
#Add a title
plt.suptitle('Pair Plot of Age, Fare, and Passenger Class', y=1.00)
#display
plt.show()