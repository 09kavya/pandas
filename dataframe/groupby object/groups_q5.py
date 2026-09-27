# find the highest rated movie of each genre
import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
genre = movie.loc[movie.groupby('Genre')['IMDB_Rating'].idxmax(),['Genre', 'Series_Title', 'IMDB_Rating']].head(1)

print(genre)