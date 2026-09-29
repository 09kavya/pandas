# find top 3 studiums with highest sixes/match ratio
import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\matches.csv")
match=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")

temp=match.merge(ipl,left_on='match_id',right_on='id')
a=temp[temp['batsman_runs']==6]
#sixes per stadium

b=a.groupby('venue')['venue'].count()
c=ipl['venue'].value_counts()
d=(b/c).sort_values(ascending=False).head(3)
print(d)