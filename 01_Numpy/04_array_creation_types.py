import numpy as np

# All 0s matrix
print(np.zeros(5))

print(np.zeros((2,3)))

print(np.zeros((2,3,3,2)))


# All 1s matrix

print(np.ones(4))

print(np.ones((2,3)))

print(np.ones((2,5,2,3)))



#Any other number  ((shape), value)
print(np.full((2,3),99))

print(np.full((2,3),99, dtype = 'float32' ))


# Other (full_like)
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])


print(np.full_like(a,4))


#Random decimal numbers

print(np.random.random_sample(a.shape))

print(np.random.rand(4,2))

#for int values

print(np.random.randint(2,7,size=(3,3)))


#Identity matrix
print(np.identity(4))

print('\n')

arr =np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)




#challenge all edges 1 and middle 0 adn centre 9

output = np.ones((5,5))
print(output)

z=np.zeros((3,3))
z[1,1] = 9
print(z)


output[1:-1,1:4] = z
print(output)



d = np.array([1,2,3])
e = d.copy()
e[0] = 100

print(e)