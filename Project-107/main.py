#importing modules
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px
import csv

#reading the csv
df = pd.read_csv("data.csv")

#printing the mean using groupby method
print(df.groupby('level')['attempt'].mean())

#drawing the bar graph
fig = go.Figure(go.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ['level1', 'level2', 'level3', 'level4'],
    orientation = 'h'
))
fig.show()

#making the scatter graph
fig2 = px.scatter(df , x= "level" , y="attempt")
fig2.show()