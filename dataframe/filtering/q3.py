#how many matches has csk won in kolkata

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")

a=ipl[ipl["City"]=="Kolkata"]&[ipl["WinningTeam"]=="Chennai Super Kings"].shape[0]

print(a)