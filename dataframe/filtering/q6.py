#Action movie with rating higher than 7.5

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
movies=movie[(movie['genres'].str.split('|').apply(lambda x: "Action" in x))& (movie['imdb_rating']>7.5)]
"""
contain: easy way
movies=movie[(movie['genres'].str.contain("Action"))& (movie['imdb_rating']>7.5)]

"""
print(movies)
