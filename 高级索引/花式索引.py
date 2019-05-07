'''
利用整数，进行索引
'''
import numpy as np

# 1： 传入顺序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[4, 2, 1, 7]])
print('\n----------1--------------\n')

# 2:传入倒序索引数组
y = np.arange(32).reshape((8, 4))
print(x[[-4, -2, -1, -7]])
print('\n----------2--------------\n')

#  3： 传入倒序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[-4, -2, -1, -7]])
print('\n---------3---------------\n')

#  4:传入多个索引数组（使用np.ix）
z = np.array(32).reshape((8, 4))
print(z[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
print('\n---------4---------------\n')

