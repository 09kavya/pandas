# 4. Plot bar chart for revenue/course


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")

a=pd.concat([regs,reg],ignore_index=True)

b=a.merge(courses,on='course_id').groupby('course_name')[['course_name','price']].sum()

b.plot(kind='bar')

plt.xlabel('Course_name')
plt.ylabel('Revenue')
plt.title('Revenue per Course')
plt.show()
