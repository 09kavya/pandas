import numpy as np
import pandas as pd

courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")

a=courses.merge(regs,how='left',on='course_id')
print(a)