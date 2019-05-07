'''
 通过一个布尔数组来索引目标数组。
 布尔索引通过布尔运算（如：比较运算符）来获取符合指定条件的元素数组。
'''

import numpy as  np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('布尔运算')
print(x)
print('大于5的元素：')
print(x[x > 5])

print('---------------------')
print('使用 ~ (取补运算符)来过滤NaN')
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
b = a[~np.isnan(a)]
print(b)

print('--------------------')
print('过滤掉非负数元素：')
d = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(d[np.iscomplex(d)])


