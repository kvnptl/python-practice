import numpy as np
np.set_printoptions(legacy='1.13')
'''

# Sample code

# 8 X 7 Dimensional array with first upper diagonal 1.
print(numpy.eye(8, 7, k=1))

#Output
[[0.  1.  0.  0.  0.  0.  0.]
 [0.  0.  1.  0.  0.  0.  0.]
 [0.  0.  0.  1.  0.  0.  0.]
 [0.  0.  0.  0.  1.  0.  0.]
 [0.  0.  0.  0.  0.  1.  0.]
 [0.  0.  0.  0.  0.  0.  1.]
 [0.  0.  0.  0.  0.  0.  0.]
 [0.  0.  0.  0.  0.  0.  0.]]

# 8 X 7 Dimensional array with second lower diagonal 1.
print(numpy.eye(8, 7, k=-2))

# Output
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0.]]
'''

ip = [int(i) for i in input().split()]

print(np.eye(ip[0], ip[1], k=0))
