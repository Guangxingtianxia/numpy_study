'''
 测试numpy的title 函数
'''

import numpy as np

a = np.array([0, 1, 2])
b = np.tile(a, (4, 1))
print('after  the arrar a invoked funcation title():', b, '\n')

c = np.array([
    [1, 2],
    [3, 4]
])

c_title_1 = np.tile(c, (4, 1))
c_title_2 = np.tile(c, 2)
print('after  the arrar c invoked funcation title():', c_title_1, '\n')
print('after  the arrar c invoked funcation title():', c_title_2, '\n')
