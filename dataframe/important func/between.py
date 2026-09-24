#work in series
import numpy as np
import pandas as pd

ipl=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv")
vk=ipl.between(51,100)
print(vk)