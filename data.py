import plotly.express as px
import pandas as pd
import csv

df = pd.read_csv('Copy+of+data+-+data.csv')
fig = px.scatter(df, x='date', y='cases', color='country',title='num of cases', size_max=60 )
fig.show()
