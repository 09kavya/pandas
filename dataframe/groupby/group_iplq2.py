# find the batsman with max no of sixes

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")
six=ipl[ipl['batsman_runs']==6]
a=six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0]
print(a)