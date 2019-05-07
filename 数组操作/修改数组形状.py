import numpy as np

a = np.arange(8)
print('tne raw array:')
print(a)

b = a.reshape(4, 2)
print('after edit:')
print(b)

''''
 numpy.ndarray.flat
'''
b = np.arange(9).reshape(3, 3)
print('raw arrar of b :', b)
for row in b:
    print(row)
# 对数组中每个元素都进行处理，可以用flat属性，改属性是一个数组元素迭代器：
print("迭代以后的数组：")
for element in b.flat:
    print(element)

print('\n=分割线================')
'''
numpy.flatten(order='C')
返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
'''

#  2行4列
c = np.arange(8).reshape(2, 4)
print("the raw array c :", c)
print('展开的数组：', c.flatten())

print('\n=分割线================')
'''
numpy.ravel() 展平的数组元素，顺序通常是'C风格'，返回的是数组视图（view ，优先类似c/c++引用reference 的意味），修改会影响原始数组
该函数可接受两个参数：numpy.rvael(a,order= 'C')
 order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。

'''
d = np.arange(8).reshape(2, 4)
print('the raw array d:')
print(d)
print('调用ravle（）函数以后：', d.ravel())
# print('以F风格顺序调用ravel 函数之后:',d.ravel(ord('F')))

# print('以K风格顺序调用ravel 函数之后:',d.ravel(ord('K')))

# print('以C风格顺序调用ravel 函数之后:',d.ravel(ord('C')))

print('以A风格顺序调用ravel 函数之后:',d.ravel(ord('A')))
