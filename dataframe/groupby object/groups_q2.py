# find the top 3 genres by total earning

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
genre=movie.groupby('Genre')['Gross'] .sum().sort_values(ascending=False).head(3)
print(genre)

