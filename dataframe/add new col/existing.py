import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
movie=movie.dropna()
movie['lead actor']=movie['actors'].str.split('|').apply( lambda x:x[0])
print(movie)