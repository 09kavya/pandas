#find all the final winner
import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
# print(ipl.head())
"""
    in one line

    ipl[ipl['MatchNumber']=="Final"][['Season','WinningTeam']]
"""
mask=ipl["MatchNumber"]=="Final"
new_df=ipl[mask]
print(new_df[['Season','WinningTeam']])