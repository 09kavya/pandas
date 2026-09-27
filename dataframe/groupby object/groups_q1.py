# Applying builtin aggregation fuctions on groupby objects
import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
genre=movie.groupby('Genre')
a=genre.sum()

print(a)
a=genre.min()
print(a)
a=genre.mean()
print(a)
a=genre.std()
print(a)