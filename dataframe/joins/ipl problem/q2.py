# find orange cap holder of all the seasons

import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\matches.csv")
match=pd.read_csv(r"C:\Users\Lenovo\Downloads\deliveries.csv")

temp=match.merge(ipl,left_on='match_id',right_on='id')
a=temp.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs',ascending=False).drop_duplicates(subset=['season'],keep='first').sort_values('season')
print(a)