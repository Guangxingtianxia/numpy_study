'''
 将元组列表转换为ndarray
'''

import numpy as np

x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)
print("--------------------")

y = [1, 2, 3]
b = np.asarray(y, dtype=float)
print(b)
