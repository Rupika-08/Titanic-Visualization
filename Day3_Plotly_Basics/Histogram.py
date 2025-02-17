import plotly.express as px
import plotly.graph_objects as go
# Load Iris dataset
df = px.data.iris()
#Display the first few rows
print(df.head())
# Histogram for sepal length
fig = px.histogram(df, x='sepal_length', color='species', title='Distribution of Sepal Length')
#Display the plot
fig.show()