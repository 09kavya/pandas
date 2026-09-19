import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\bollywood.csv",index_col="movie")
print(a)

b=a.loc['2 States (2014 film)']
print(b)