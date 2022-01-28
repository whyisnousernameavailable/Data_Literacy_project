import numpy as np
import matplotlib.pyplot as plt
from tueplots import bundles

from Python_Code.definitions import load_caracteristics_csv, load_places_csv, load_holidays_csv, load_users_csv, \
    load_vehicles_csv

plt.rcParams.update(bundles.neurips2021(usetex=False))

test = np.array((8, 1, 10, -5, -4, 7))
plt.plot(test)
plt.show()

data_characteristics = load_caracteristics_csv()
data_places = load_places_csv()
data_holidays = load_holidays_csv()
data_users = load_users_csv()
data_vehicles = load_vehicles_csv()

print(data_places.head())
print(data_characteristics.head())
print(data_users.head())
print(data_vehicles.head())
print(data_holidays.head())
print(data_characteristics['an'].value_counts())

data_characteristics['an'].value_counts().sort_index().plot(kind='bar')
plt.savefig('..//Plots//Accidents_per_an.pdf', format='pdf')
plt.show()

