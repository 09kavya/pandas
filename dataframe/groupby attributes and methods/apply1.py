# find number of movies starting with A for each group

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby('Genre')

def foo(group):
    return  group['Series_Title'].str.startswith('A').sum()
    

group=a.apply(foo)
print(group)