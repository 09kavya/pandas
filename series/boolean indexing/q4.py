#find actors who have done more than 20 movies 

import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\bollywood.csv",index_col="movie")
b=a.value_counts()
c=b[b>20]
print(c)