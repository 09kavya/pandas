#find no of ducks(0)

import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv",index_col="match_no")
b=a[a['runs']==0]
print(b)