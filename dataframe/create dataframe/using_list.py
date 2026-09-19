import numpy as np
import pandas as pd

student_list=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]


a=pd.DataFrame(student_list,columns=['iq','marks','package'])
print(a)