import numpy as np
import pandas as pd

marks={
   
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
mark=pd.Series(marks)
a=mark.sort_index()
print(a)
a=mark.sort_index(ascending=False)
print(a)