#Name: Aliasghar Rashidabadi    
#Student ID: 4041955
#Course: Advanced Programming

import numpy as np

hi = np.array([[96, 15, 80, 4],[49, 43, 96, 85], [81, 92, 66, 94]])
hi_reshaped = hi.reshape(6, 2)
bye = np.transpose(hi_reshaped)
print(bye)