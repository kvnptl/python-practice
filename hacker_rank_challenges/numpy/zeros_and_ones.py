import numpy as np

'''
# Sample code

print numpy.zeros((1, 2))  # Default type is float
# Output : [[ 0.  0.]]

print numpy.zeros((1, 2), dtype=numpy.int)  # Type changes to int
# Output : [[0 0]]

print numpy.ones((1,2))                    #Default type is float
# Output : [[ 1.  1.]]

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
# Output : [[1 1]]
'''

ip = [int(i) for i in input().split()]
ip = tuple(ip)
print(np.zeros(ip, np.int64))
print(np.ones(ip, np.int64))
