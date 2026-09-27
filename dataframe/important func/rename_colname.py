import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
a=movie.set_index('title_x').rename(index={'Uri: The Surgical Strike':'Uri'})
print(a)