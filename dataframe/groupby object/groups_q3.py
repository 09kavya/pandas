# find the genre with highest avg IMDB rating

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
# print(movie.columns)
genres=movie.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1)

print(genres)