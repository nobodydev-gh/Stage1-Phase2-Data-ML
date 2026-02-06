import numpy as np
#### MISCELLANEOUS ####

# load data from file

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)


