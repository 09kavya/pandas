import numpy as np
import pandas as pd

temp=pd.Series([1,2,np.nan,4,np.nan,5,6,np.nan,8])
a=temp.size
print(a)
a=temp.count()
print(a)
a=temp.isnull().sum()
print(a)