#work in series and dataframe

import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
a=ipl['Season'].nunique()
print(a)