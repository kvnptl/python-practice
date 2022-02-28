import numpy as np

ip = [int(i) for i in input().split()]

a, b = [], []
for _ in range(ip[0]):
    a.append([int(j) for j in input().split()])
for _ in range(ip[0]):
    b.append([int(j) for j in input().split()])

a = np.array(a)
b = np.array(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)
print(a**b)
