import numpy

n, m = input().split()

temp_list = []
for i in range(int(n)):
    num = map(int, input().split())
    temp_list.append(list(num))

l = numpy.array(temp_list)
flat_list = l.flatten()
np_list = numpy.reshape(flat_list, (int(n), int(m)))
print(np_list.transpose())
print(flat_list)
