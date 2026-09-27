# find director with most popularity

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
# print(movie['No_of_Votes'])
director=movie.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)
print(director)
