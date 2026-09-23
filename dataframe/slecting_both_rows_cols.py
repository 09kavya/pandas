import numpy as np
import pandas as pd

import numpy as np
import pandas as pd

student_dict={
    "name":["nitish","abhay","sagar","pooja"],
    'iq':[100,90,120,80],
    'marks':[80,70,100,50],
    'package':[10,7,14,2]
}

a=pd.DataFrame(student_dict)
b=a.set_index("name")
print(a.iloc[0:3,0:3])