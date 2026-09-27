import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby(['Genre','Star1'])

#size
b=a.size()
print(b)

#get_group
b=a.get_group(('Drama','Amole Gupte'))
print(b)