# find the best(in-terms of metascore(avg)) actor->genre combo

import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby(['Genre','Star1'])
b=a['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1)
print(b)
