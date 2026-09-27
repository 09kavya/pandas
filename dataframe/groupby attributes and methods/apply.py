"""
split (apply) combine

"""
import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby('Genre')
b=a.apply(min)
print(b)