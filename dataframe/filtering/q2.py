#how many super over finishes have occured
import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
# print(ipl.columns)

a=ipl[ipl['SuperOver']=="Y"].shape[0]
print(a)