#toss winner is match winner in percentage
import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
a=(ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0])*100
print(a)