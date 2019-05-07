'''
 运算形状不同的数组时，就会触发广播机制
'''

import numpy as np

a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])

b = np.array([1, 2, 3])

c = a * b
d = a + b
print('a * b=', c, '\n')
print('a + b=', d, '\n')

bb = np.tile(b, (4, 1))

print('bb=',  bb, '\n')
print('a+bb=', a + bb, '\n')
