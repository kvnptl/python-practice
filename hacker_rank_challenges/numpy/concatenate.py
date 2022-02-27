import numpy as np

'''
# Sample code

array_1 = numpy.array([[1, 2, 3], [12, 13, 14]])
array_2 = numpy.array([[0, 0, 0], [7, 8, 9]])

# concatenate on row
print(numpy.concatenate((array_1, array_2), axis=0))

#concatenate on column
print(numpy.concatenate((array_1, array_2), axis=1))
'''

n, m, p = input().split()

temp_list = []
for i in range(int(n)):
    a = map(int, input().split())
    temp_list.append(list(a))

np_a = np.array(temp_list)
temp_list = []
for i in range(int(m)):
    a = map(int, input().split())
    temp_list.append(list(a))
np_b = np.array(temp_list)

print(np.concatenate((np_a, np_b), axis=0))
