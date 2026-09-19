import numpy as np
import pandas as pd

marks=[67,57,89,100]
subjects=['Maths','English','Science','Hindi']
a = pd.Series(marks, index=subjects)
a[2:4]=[100,100]
print(a)