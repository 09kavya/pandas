import numpy as np 
import pandas as pd

marks=[67,57,89,100]
subjects=['Maths','English','Science','Hindi']
a = pd.Series(marks, index=subjects)

a[[0,2,3]]=75
print(a)