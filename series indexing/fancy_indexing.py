import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv",index_col="match_no")
print(a)

b=a.loc[[1,58,96,214,22,100,123]]
print(b)