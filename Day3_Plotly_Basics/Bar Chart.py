import plotly.express as px
import plotly.graph_objects as go
# Load Iris dataset
df = px.data.iris()
#Display the first few rows
print(df.head())
# Bar chart for average petal length by species
fig = px.bar(df, x='species', y='petal_length', color='species', title='Average Petal Length by Species')
# Display the plot
fig.show()