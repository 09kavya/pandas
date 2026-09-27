import numpy as np
import pandas as pd

movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\imdb-top-1000.csv")
a=movie.groupby('Genre')
b=a.agg({
    'Runtime':'mean',
    'IMDB_Rating':'mean',
    'No_of_Votes':'sum',
    'Gross':'sum',
    'Metascore':'min'
})
print(b)
#passing list
b=a[['Runtime', 'IMDB_Rating', 'No_of_Votes', 'Metascore']].agg(['mean','min','max','sum'])
print(b)