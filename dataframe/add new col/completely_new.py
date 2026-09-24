import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
movie['country']="India"
print(movie)