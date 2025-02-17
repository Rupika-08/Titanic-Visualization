import seaborn as sns
import matplotlib.pyplot as plt
#Seaborn comes with built-in datasets.
#Load titanic dataset
titanic = sns.load_dataset('titanic')
#Display the first few rows
print(titanic.head())
