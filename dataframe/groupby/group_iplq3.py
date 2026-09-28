# find batsman with most number of 4's and 6's in last 5 overs

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")
match=ipl[ipl['over']>15]
match=match[(match['batsman_runs']==4) | (match['batsman_run']==6)]
a=match.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0]
print(a)