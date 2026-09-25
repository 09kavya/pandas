import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipl = pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")

match = ipl["TossDecision"].value_counts()

a=match.plot(kind="pie")


plt.show()