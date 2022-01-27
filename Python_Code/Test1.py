import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Python_Code.definitions import dtype_caracteristics, dtype_places, dtype_vehicles, dtype_users, dtype_holidays

test = np.array((8, 1, 10, -5, -4, 7))
plt.plot(test)
plt.show()

data_characteristics = pd.read_csv('..//archive//caracteristics.csv',
                                   encoding="ISO-8859-1", dtype=dtype_caracteristics,
                                   on_bad_lines='warn', na_values=['-'])
data_places = pd.read_csv('..//archive//places.csv',
                                   encoding="ISO-8859-1", dtype=dtype_places,
                                   on_bad_lines='warn', na_values=['-'])
data_holidays = pd.read_csv('..//archive//holidays.csv',
                                   encoding="ISO-8859-1", dtype=dtype_holidays,
                                   on_bad_lines='warn', na_values=['-'], parse_dates=['ds'])
data_users = pd.read_csv('..//archive//users.csv',
                                   encoding="ISO-8859-1", dtype=dtype_users,
                                   on_bad_lines='warn', na_values=['-'])
data_vehicles = pd.read_csv('..//archive//vehicles.csv',
                                   encoding="ISO-8859-1", dtype=dtype_vehicles,
                                   on_bad_lines='warn', na_values=['-'])
print(data_places.head())
print(data_characteristics.head())
print(data_users.head())
print(data_vehicles.head())
print(data_holidays.head())


data_characteristics['an'].value_counts().plot(kind='bar')
plt.show()
plt.savefig('..//Plots//Accidents_per_an.pdf')

