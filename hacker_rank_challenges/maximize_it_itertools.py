from itertools import product
k, m = input().split()

lists = []
temp_list = []
for i in range(int(k)):
    nums = input().split()
    lists.append([int(i) for i in nums[1:]])

max_val_list = []

#for testing
# a = [[1,2,3], [4,5], [6,7]]

'''
Ref: https://stackoverflow.com/a/11315061/6920365

In Python, *variable means: 
* unpacks a list or tuple into position arguments.

** unpacks a dictionary into keyword arguments.
'''

# What is python itertools?
# Ref: https://www.geeksforgeeks.org/python-itertools/

d = list(product(*lists))

for i in d:
    sum = 0
    for j in i:
        sum += j**2
    max_val_list.append(sum%int(m))


print(max(max_val_list))
