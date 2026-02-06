import numpy as np

#BASICS
a=np.array([1,2,3])
print(a)

b=np.array([[9.0,8.9,2.3],[4.3,6.1,1.2]])
print(b)

#Get dimensions
print(a.ndim)

#Get Shape 
print(a.shape)
print(b.shape)


#Get Type
print(a.dtype)
print(b.dtype)

#to specify type
c=np.array([1,2,3], dtype='int16')

#get type
print(c.dtype)


#Get Size
print(a.itemsize)
print(c.itemsize)


#Get Total size
print(a.size*a.itemsize)
 #or
print(a.nbytes)