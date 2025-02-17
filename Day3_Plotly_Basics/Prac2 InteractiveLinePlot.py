import plotly.express as px
import plotly.graph_objects as go
# Load the data set
df = px.data.stocks()
# Print the data
print(df.head())
# Create scatter plot that shows google and microsoft stock prices
fig = px.line(df, x='date', y=['GOOG', 'MSFT', 'AAPL'], title='Google vs Microsoft Stock Prices Over Time')
# Display the plot
fig.show()