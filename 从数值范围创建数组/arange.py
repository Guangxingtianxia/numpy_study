"""
numpy.arange(start, stop, step, dtype)
     arange ([start,] stop[, step,], dtype=None)

参数	描述
start	起始值，默认为0
stop	终止值（不包含）
step	步长，默认为1
dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。


"""

#  生成0到5 的数组
import numpy as np

x = np.arange(5)
print(x)

#  返回类型为float：
#  设置了dtype
y = np.arange(5, dtype=float)
print(y)

# 设置起始值，终止值 ，步长
z = np.arange(10, 20, 2)
print(z)
