# find the top 10 batsman in terms of runs

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")
a=ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(a)