#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import numpy as np

x_value = np.pi / 2
h = 1e-10

derivative = (np.sin(x_value + h) - np.sin(x_value))/h

print(derivative)