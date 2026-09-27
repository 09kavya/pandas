import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby('Genre').first()
print(a)

a=movie.groupby('Genre').last()
print(a)

a=movie.groupby('Genre').nth(1)
print(a)