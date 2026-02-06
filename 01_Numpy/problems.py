import numpy as np



a = np.arange(1, 31).reshape(6, 5)
print(a)


print('\n')
print(a[2:3,0:1])

print(a[[0,1,2,3],[1,2,3,4]])

print(a[[0,4,5],3:])

