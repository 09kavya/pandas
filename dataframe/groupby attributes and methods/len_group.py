#find total number of groups

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=len(movie.groupby('Genre'))
print(a)
a=movie['Genre'].nunique()
print(a)