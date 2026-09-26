import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
sort=movie.sort_values(['year_of_release','title_x'])
print(sort)
sort=movie.sort_values(['year_of_release','title_x'],ascending=[True,False])
print(sort)