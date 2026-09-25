import numpy as np
import pandas as pd

vk=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv")
out=vk[vk['runs'].isin([49,99])]
print(out)