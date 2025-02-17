import plotly.express as px
import plotly.graph_objects as go
# Load Iris dataset
df = px.data.iris()
#Display the first few rows
print(df.head())
# Scatter plot for sepal width vs sepal length
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Sepal Width vs Sepal Length')
# Display the plot
fig.show()