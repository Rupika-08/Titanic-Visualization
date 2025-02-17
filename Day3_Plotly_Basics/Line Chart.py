import plotly.express as px
import plotly.graph_objects as go
# Load Iris dataset
df = px.data.iris()
#Display the first few rows
print(df.head())
#Line chart for petal width by species
fig = px.line(df, x='species', y='petal_width', color='species', title='Petal Width by Species')
# Display the plot
fig.show()