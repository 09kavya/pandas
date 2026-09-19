import numpy as np
import pandas as pd

student_dict={
    'iq':[100,90,120,80],
    'marks':[80,70,100,50],
    'package':[10,7,14,2]
}

a=pd.DataFrame(student_dict)
print(a)