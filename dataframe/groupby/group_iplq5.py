# Create a function that can return the highest score of any batsman

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")
temp=ipl[ipl['batsman']=='V Kohli']
temp=temp.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

def highest(batsman):
    temp=ipl[ipl['batsman']==batsman]
    return temp.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

a=highest('DA Warner')
print(a)