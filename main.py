"""
STEM Model 2021 for Representing Methane Production
Copyright (C) 2021 Carlos Miller 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
import graphs
from data_management import *
import matplotlib.pyplot as plt



"""
General Slurry Data:
                |   Trial  1   |  Trial  2  | ...
================|==============|============|
Start Volume    |    (int)     |            | ...
================|==============|============|
Acidity         |    (int)     |            | ...
================|==============|============|
Blended         |    (bool)    |            | ...
================|==============|============|

Slurry Mass (TRIAL 1):
                |   Gas Vol.   |  Slurry Vol.  | 
================|==============|===============|
(time.obj)      |    (int)     |     (int)     |
================|==============|===============|
...             |              |               | 
================|==============|===============|

data/
    slurry_mass.npz
    general_slurry.npz
"""
