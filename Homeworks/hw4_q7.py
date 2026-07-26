#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import numpy as np

v = np.ones(11, dtype = np.int8)
v[1::2] = np.arange(9,-4,-3)
v[::2] = np.arange(1,12,2)

print(v)