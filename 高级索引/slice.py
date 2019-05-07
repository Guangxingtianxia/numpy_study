import numpy as np

a = np.arange(10)

# 从索引2开始检索 7停止，间隔为2
s = slice(2, 7, 2)
print(a[s])

alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
var = alist[1:5:2]
print(var)

#  获取数组中(0,0)，(1,1)和(2,0)位置处的元素。
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)


