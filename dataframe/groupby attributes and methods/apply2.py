# find ranking of each movie in the group according to IMDB score

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby('Genre')

def foo(rank):
    rank['genre_rank']=rank['IMDB_Rating'].rank(ascending=False)
    return rank
rank=a.apply(foo)
print(rank)