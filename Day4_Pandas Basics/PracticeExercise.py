import pandas as pd 
#Load Titanic dataset from a URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#Display the first 5 rows of the dataset
print(df.head)

# Filter the Dataset:

# Filter passengers who survived (Survived == 1)
survivors = df[df['Survived'] == 1]
print("Survivors:")
print(survivors.head())

# Filter passengers in first class (Pclass == 1)
first_class_passengers = df[df['Pclass'] == 1]
print("\nFirst Class Passengers:")
print(first_class_passengers.head())

# Create new columns:

# Create the IsChild column
df['IsChild'] = df['Age'] < 18
print("\nIsChild Column:")
print(df[['Age', 'IsChild']].head())

# Create the FareCategory column
df['FareCategory'] = pd.cut(df['Fare'], bins=[0, 10, 50, float('inf')], labels=['Low', 'Medium', 'High'])
print("\nFareCategory Column:")
print(df[['Fare', 'FareCategory']].head())

# Analyzing the Data

# Calculate the survival rate for children (IsChild == True)
child_survival_rate = df[df['IsChild']]['Survived'].mean()
print(f"\nChild Survival Rate: {child_survival_rate:.2%}")

# Calculate the average fare for each FareCategory
average_fare_by_category = df.groupby('FareCategory')['Fare'].mean()
print("\nAverage Fare by Category:")
print(average_fare_by_category)

