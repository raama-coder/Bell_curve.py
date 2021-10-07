import csv
import pandas as pd
import plotly.figure_factory as pf

df=pd.read_csv("/Users/raama/Documents/White hat jr./python/p108/data.csv")

fig=pf.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()