'''
 函数-----------------------> 描述：
transpose                    对换数组的维度
ndarray.T                    和self.transpose() 相同
rollaxis                     向后滚动指定的轴
swapaxes                     对换数组的两个轴
'''

import numpy as np

a = np.arange(12).reshape(3, 4)

print('the raw array:')
print(a)

"""
numpy.transpose(arr, axes)
arr：要操作的数组
axes：整数列表，对应维度，通常所有维度都会对换。
"""
print('对换数组：')
print(np.transpose(a))
