#how mny matches each team has played

import numpy as np 
import pandas as pd

ipl = pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
match=ipl['Team1'].value_counts()+ipl['Team2'].value_counts()
print(match.sort_values(ascending=False))