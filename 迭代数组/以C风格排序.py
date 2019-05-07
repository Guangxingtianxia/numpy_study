import numpy as np

a = np.arange(0, 60, 5)
print("the raw array by arange():", a)
a = a.reshape(3, 4)
print("the raw array by reshape():", a)
print("以C风格顺序排序：")
for x in np.nditer(a, order='C'):
    print(x, end='')

print('\n')
