# 7. find students who did not enroll into any courses

import numpy as np
import pandas as pd

courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")

a=pd.concat([regs,reg],ignore_index=True)

temp=np.setdiff1d(students['student_id'],a['student_id'])
b=students[students['student_id'].isin(temp)].shape[0]

print((10/28)*100)