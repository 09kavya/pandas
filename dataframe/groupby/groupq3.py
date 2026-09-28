# agg on multiple groupby

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby(['Director','Star1'])
b=a[['Gross', 'IMDB_Rating']].agg(['mean','sum','min'])
print(b)