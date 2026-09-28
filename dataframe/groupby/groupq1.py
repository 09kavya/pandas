# find the most earning actor->director combo

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby(['Director','Star1'])
b=a['Gross'].sum().sort_values(ascending=False).head(1)
print(b)