"""
NM Stem Challenge Model

Author: Carlos Miller 
Written on: Nov. 13 2021
Version: 0.1 (Nov. 15 2021)
"""

from turtle import *
from random import randint
import numpy as np
import itertools
import pickle
import threading
import time

start = time.perf_counter()

finish = time.perf_counter()

print("Executed in", str(round((finish - start), 2)), "(s)")

"""
(1) C6H1206 -> 2 Et + 2 CO2, with 2 CO2 making up 25% of atoms "lost" during
fermentation. But, most yeasts can only survive in less than 18% alcohol
before dying to toxicity. Therefore, 100ml of glucose/sucrose could take up
to 10 runs to fully process if the slurry is distilled @ 10% alcohol.

Bypassing true volume and settling for theoretical atomic volume (if all
atoms are equally sized in space at all pressures and temperatures) then
the end result of the Fermentation Model is 75% of the starting volume in
ethanol, and 25% in carbon dioxide.

Inconsistencies in food waste introduce complexities to the simulation. Our
model will either take an average sugar content of multiple biofuel batches
or generalize it as done with simulated volume.

Distillation will be presented with the same simplicity as volume and 
sugar content. The process will be simulated as such:
    Near poisoned yeast strained from biomass-ethanol mixture >>
    heat the mixture towards the boiling point of ethanol >>
    ethanol evaporates and condenses into near pure ethanol >>
    remaining biomass is cooled and the fermentation process begins again.
    
"""
