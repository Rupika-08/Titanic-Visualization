import seaborn as sns
import matplotlib.pyplot as plt
#Seaborn comes with built-in datasets.
#Load titanic dataset
titanic = sns.load_dataset('titanic')
#Display the first few rows
print(titanic.head())
#count plot for 'sex' column
sns.countplot(x='sex', data=titanic, palette='viridis')
#add labels and title
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Passenger Count by Gender')
#Display the plot
plt.show()