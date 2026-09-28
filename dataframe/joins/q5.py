# 5. find students who enrolled in both the months
import numpy as np
import pandas as pd
courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")

a=pd.concat([regs,reg],ignore_index=True)
 
registration=np.intersect1d(regs['student_id'],reg['student_id'])
print(registration)

a=students[students['student_id'].isin(registration)]
print(a)