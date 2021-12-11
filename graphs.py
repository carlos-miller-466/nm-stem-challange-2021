from data_management import *
from data_gen import Data

DATA = Data()

import matplotlib.pyplot as plt

### TRIAL 1
dbt = diffs_between_times(DATA.trial1_timestamps)
trial1 = []

for gas1, gas2, t in zip(*[iter(DATA.trial1_growing[:,0])]*2, dbt): trial1.append(np.linspace(gas1, gas2, round(t)))

trial1 = np.concatenate((trial1[0], trial1[1]))

plt.plot(range(trial1.shape[0]), trial1)
plt.title("Trial 1, Gas over time")
plt.xlabel("Hour of experiment")
plt.ylabel("Methane Generated (mL)")

plt.show()

### TRIAL 2
dbt = diffs_between_times(DATA.trial2_timestamps)
trial2 = []

for gas1, gas2, t in zip(*[iter(DATA.trial2_growing[:,0])]*2, dbt):
    trial2.append(np.linspace(gas1, gas2, round(t)))

trial2 = np.concatenate((trial2[0], trial2[1]))

plt.plot(range(trial2.shape[0]), trial2)
plt.title("Trial 2, Gas over time")
plt.xlabel("Hour of experiment")
plt.ylabel("Methane Generated (mL)")

plt.show()

### TRIAL 3
dbt = diffs_between_times(DATA.trial3_timestamps)
trial3 = []

for gas1, gas2, t in zip(*[iter(DATA.trial3_growing[:,0])]*2, dbt):
    trial3.append(np.linspace(gas1, gas2, round(t)))

trial3 = np.concatenate((trial3[0], trial3[1]))

plt.plot(range(trial3.shape[0]), trial3)
plt.title("Trial 3, Gas over time")
plt.xlabel("Hour of experiment")
plt.ylabel("Methane Generated (mL)")

plt.show()

### TRIAL 4
dbt = diffs_between_times(DATA.trial4_timestamps)
trial4 = []

for gas1, gas2, t in zip(*[iter(DATA.trial4_growing[:,0])]*2, dbt):
    trial4.append(np.linspace(gas1, gas2, round(t)))

trial4 = np.concatenate((trial4[0], trial4[1]))

plt.plot(range(trial4.shape[0]), trial4)
plt.title("Trial 4, Gas over time")
plt.xlabel("Hour of experiment")
plt.ylabel("Methane Generated (mL)")

plt.show()
