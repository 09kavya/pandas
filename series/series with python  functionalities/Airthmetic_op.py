#broadcasting work

import numpy as np
import pandas as pd

marks=[67,57,89,100]
subjects=['Maths','English','Science','Hindi']
a = pd.Series(marks, index=subjects)

b=100-a
print(b)