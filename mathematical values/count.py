import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv",index_col="match_no",dtype=np.int16)
b=a.count()
print(b)