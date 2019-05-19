"""
numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
numpy.rollaxis(arr, axis, start)

参数说明：

arr：数组
axis：要向后滚动的轴，其它轴的相对位置不会改变
start：默认为零，表示完整的滚动。会滚动到特定位置。

"""

import numpy as np

#  创建一个3维数组
a = np.arange(8).reshape(2, 2, 2)
print("3维数组：")
print(a)
'''

[ 
 [
    [0 1]
    [2 3]
 ]

 [
    [4 5]
    [6 7]
 ]
]



'''
