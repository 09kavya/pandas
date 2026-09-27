import numpy as np
import pandas as pd

temp=pd.Series([1,1,2,4,5,2,4,8,6,7,6,3,9,5,np.nan])
a=temp.unique()
print(a)