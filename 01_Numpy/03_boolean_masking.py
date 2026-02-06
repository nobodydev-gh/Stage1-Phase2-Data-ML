import numpy as np


filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)


print(filedata[filedata > 50])


print(filedata > 50)

print('\n')

print(np.any(filedata > 50, axis=0))


print('\n')

print(np.all(filedata > 50, axis=0))

print('\n')

print((filedata > 50) & (filedata < 100))


print('\n')

print(~(filedata > 50) & (filedata < 100))



#index with a list in numpy

a = np.array([1,2,3,4,5,6,7,8,9])

print(a[[1,2,8]])







