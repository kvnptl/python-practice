import numpy as np

n = int(input())

temp_list = []
for i in range(n):
    ip = map(float, input().split())
    l = list(ip)
    temp_list.append(l)

mat_a = np.reshape(temp_list, (-1, len(temp_list)))
print(round(np.linalg.det(mat_a), 2))
