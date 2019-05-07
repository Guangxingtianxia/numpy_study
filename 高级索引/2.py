import numpy as np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('数组是 : ')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
clos = np.array([[0, 2], [0, 2]])

#  获取4X3数组中的4个元素，行索引是[0,0]和[3,3],而列索引是[0,2]和[0,2]
y = x[rows, clos]
print('这个数组的四个元素是：')
print(y)
# 返回的结果是包含每个元素的ndarray对象
# 可以借助切片 : 或 ... 与索引数组组合.

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
d = a[..., 1:]
print(a)
print(b)
print(c)
print(d)
