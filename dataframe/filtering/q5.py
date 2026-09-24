#movies with rating higher than 8 and votes>10000

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
movies=movie[(movie['imdb_rating']>8) & (movie['imdb_votes']>10000)]

print(movies)