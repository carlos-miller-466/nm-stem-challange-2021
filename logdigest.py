"""
Log Digestion 

Author: Carlos Miller
Written on: Nov. 13 2021
Version: 0.1 (Nov. 15 2021)
"""

import pickle
data = []
with open('COLLISION_DET.log', 'rb') as f_obj:
    entries = len(f_obj.readlines())
with open('COLLISION_DET.log', 'rb') as f_obj:
    for entrie in range(entries):
        print(entrie)
        try:
            data.append(pickle.load(f_obj))
        except EOFError:
            continue

for data_point in data:
    for xset, yset in zip(data_point[0],data_point[1]):
        print(data.index(data_point))
        print(xset)
        print(yset)
