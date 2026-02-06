import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)




print('\n')

#vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))

print(np.vstack([v1,v2,v2,v1]))




print('\n')
#Horizontal stacking vector

h1=np.array([[3,2,4,5],[6,2,5,3]])
h2=np.array([[6,4,7,2],[1,2,3,4]])

print(np.hstack([h1,h2]))

