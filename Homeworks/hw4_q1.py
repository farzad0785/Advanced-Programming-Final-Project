#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import numpy as np

arr = np.ones((13,13))
arr[1::5] = arr[:,1::5] = 2
arr[3:5, 3:5] = arr[8:10, 3:5] = arr[3:5, 8:10] = arr[8:10, 8:10] = 3
print(arr)