#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import numpy as np

nums = np.arange(1,11)
calculations = ((-1)**(nums - 1)) / (2**(nums - 1))
total_sum = np.sum(calculations)

print(total_sum)