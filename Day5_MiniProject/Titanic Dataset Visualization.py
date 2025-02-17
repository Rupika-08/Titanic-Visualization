import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Data cleaning
df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill missing Age values
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill missing Embarked values
df.drop('Cabin', axis=1, inplace=True)  # Drop the Cabin column (too many missing values)

# Create new columns
df['FamilySize'] = df['SibSp'] + df['Parch']  # Family size
df['IsChild'] = df['Age'] < 18  # Is the passenger a child?
df['FareCategory'] = pd.cut(df['Fare'], bins=[0, 10, 50, float('inf')], labels=['Low', 'Medium', 'High'])  # Fare categories

# Display cleaned data
print(df.head())

#VISUALIZE KEY INSIGHTS

# 1. Survival Rate by Gender (Bar CHart - Matplotlib)
# Calculate survival rate by gender
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()

# Plot
plt.figure(figsize=(8, 6))
survival_rate_by_gender.plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.show()
# 2. Age Distribution by Survival Status (Histogram - Seaborn)
# Plot
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', hue='Survived', kde=True, palette='viridis', bins=20)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
# 3. Survival Rate by Passenger Class (Bar Chart - Seaborn)
# Plot
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Pclass', y='Survived', palette='coolwarm', ci=None)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()
# 4. Fare vs. Age with Survival Status (Scatter Plot - Plotly)
# Plot
fig = px.scatter(df, x='Age', y='Fare', color='Survived', title='Fare vs. Age with Survival Status')
fig.show()
# 5. Survival Rate by Family Size (Bar Chart - Matplotlib)
# Calculate survival rate by family size
survival_rate_by_family = df.groupby('FamilySize')['Survived'].mean()

# Plot
plt.figure(figsize=(8, 6))
survival_rate_by_family.plot(kind='bar', color='teal')
plt.title('Survival Rate by Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.show()
# 6. Interactive Survival Rate by Embarkation Port (Bar Chart - Plotly)
# Calculate survival rate by embarkation port
survival_rate_by_embark = df.groupby('Embarked')['Survived'].mean().reset_index()

# Plot
fig = px.bar(survival_rate_by_embark, x='Embarked', y='Survived', title='Survival Rate by Embarkation Port')
fig.show()

# Save the Visualizations
# Save Matplotlib plots
plt.savefig('survival_rate_by_gender.png')

# Save Plotly plots
fig.write_html('fare_vs_age.html')