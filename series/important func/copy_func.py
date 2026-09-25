import numpy as np
import pandas as pd

match=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv")
match[1]=1
vk=match.head().copy()
print(vk)