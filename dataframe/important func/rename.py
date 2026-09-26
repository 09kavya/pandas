#work in dataframe
import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
a=movie.rename(columns={'imdb_id':'imdb','poster_path':'link_of_poster'})
print(a.columns)