import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Python_Code.definitions import dtype_caracteristics

test = np.array((8, 1, 10, -5, -4, 7))
plt.plot(test)
plt.show()

data_characteristics = pd.read_csv('..//archive//caracteristics.csv',
                                   encoding="ISO-8859-1", dtype=dtype_caracteristics)
print(data_characteristics.head())

