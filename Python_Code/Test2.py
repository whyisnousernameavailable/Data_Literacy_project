import numpy as np
import matplotlib.pyplot as plt
from tueplots import bundles

from Python_Code.definitions import load_caracteristics_csv, load_places_csv, load_holidays_csv, load_users_csv, \
    load_vehicles_csv

plt.rcParams.update(bundles.neurips2021(usetex=False))

data_characteristics = load_caracteristics_csv()
data_users = load_users_csv()

print(data_characteristics['an'].value_counts())
print(data_users['grav'].value_counts(normalize=True))
