import plotly.express as px
import plotly.graph_objects as go
# Load Titanic dataset from a URL
df = px.data.stocks()
# Print dataset
print(df.head())
# Create a Scatter Plot
fig = px.scatter(df, x='date', y='GOOG', title='Stock Prices Over Time')
# Display the plot
fig.show()