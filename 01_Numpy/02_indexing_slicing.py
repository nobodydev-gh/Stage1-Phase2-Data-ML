import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

print(a.shape)


#Get a specific element [r,c]
#13
print(a[1,5])
#or
print(a[1,-2])


#get specific row
print(a[0,:])


#get specific column
print(a[:,2])


#Getting a little more fancy [startindex:endindex:stepsize]
print(a[0,1:6:2])

a[1,5] = 20
print(a)

# a[:,2] = 5
# print(a)

a[:,2] = [4,2]
print(a)


#3d example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


#get specific element (work outside in)
#get the 3,4
print(b[0,1,1])
print(b[:,1,:])

#replace
b[:,1,:]=[[9,9],[8,8]]
print(b)


