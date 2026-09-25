import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")

name=movie[movie['actors'].apply(lambda a:a.split()[0].upper())]
print(name)