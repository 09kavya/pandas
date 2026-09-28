# find V Kohli's record against all teams
import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")
temp_df=ipl[ipl['batsman']=='V Kohli']
temp_df=temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index()
print(temp_df)