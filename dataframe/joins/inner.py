import numpy as np
import pandas as pd

students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")

a=students.merge(regs,how='inner',on='student_id')
print(a)