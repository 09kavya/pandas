#find normalized IMDB rating group wise


import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby('Genre')

def foo(group):
    group['norm_rating']=(group['IMDB_Rating']-group['IMDB_Rating'].min())/(group['IMDB_Rating'].max()-group['IMDB_Rating'].min())
    return group

b=a.apply(foo)
print(b)


