import numpy as np
import pandas as pd

marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

a=pd.Series(marks,name='Nitish ke marks')
print(a)