import numpy as np


a = np.array([1,2,3,4])
print(a)

print(a + 2)

print(a - 2)

print(a * 2)

print(a / 2)

b = np.array([1,0,1,0])
print(a + b)

print(a ** 2)


#take the sin
print(np.sin(a))

print(np.cos(a))



#Linear Algebra
a = np.ones((2,3))
print(a)

print('\n')

b = np.full((3,2), 2)
print(b)


print('\n')

print(np.matmul(a,b))


#Find the determinant

c = np.identity(3)
print(np.linalg.det(c))



######### STATISTICS #########


stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))

print(np.max(stats,axis=1))       ## (axis=0) == column   (axis=1) == row

print(np.sum(stats))




