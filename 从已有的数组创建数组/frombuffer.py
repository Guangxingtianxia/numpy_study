"""
numpy.formbuffer  用于实现动态数组，可接受buffer输入参数，以流的形式转化成ndarray对象；
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)

"""

import numpy as np;
s = b'Hello World'
a = np.frombuffer(s,dtype='S1')
print(a)

