#Find no of 50's and 100's scored by kohli

import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv",index_col="match_no")

b=a[a['runs']>=50]
print(b)