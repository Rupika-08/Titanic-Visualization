import seaborn as sns
import matplotlib.pyplot as plt
#Load titanic dataset
titanic = sns.load_dataset('titanic')
#Display the first few rows
print(titanic.head())
#Histogram for 'age' column
sns.histplot(titanic['age'], bins=20, kde=True, color='blue')
#Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Passengers')
#Display the plot
plt.show()