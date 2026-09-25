#find which player has won most potm -> in finals and qualifiers

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
match=ipl[~ipl['MatchNumber'].str.isdigit()]
print(match['Player_of_Match'])