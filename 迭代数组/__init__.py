'''

NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。
迭代器最基本的任务的可以完成对数组元素的访问。
控制遍历顺序
for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
for x in np.nditer(a.T, order='C'):C order，即是行序优先；


'''

import numpy as np

a = np.arange(6).reshape(2, 3)
print("The raw array :", a)
print("=孤独的分割线=================")
for x in np.nditer(a):
    print(x, end=",")
print('\n')

print("=孤独的分割线=================")
b = np.arange(6).reshape(2, 3)
for x in np.nditer(b.T):
    print(x, end=",")
print("\n")


