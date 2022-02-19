from collections import defaultdict

ddict = defaultdict(list)

# n, m = input().split()
n, m = map(int, input().split())

for i in range(n):
    ddict[input()].append(i+1)

'''
What does * in Python mean?

The * in python is used to unpack the iterable.

print(*[1,2,3]) 
#1 2 3

print(*(1,2,3))
#1 2 3

print(*"123")
#1 2 3

Ref: https://www.thepoorcoder.com/hackerrank-defaultdict-solution/
'''

for i in range(m):
    ip = input()
    if ip in ddict.keys():
        # without star
        print(ddict[ip])
        #with star
        print(*ddict[ip])
    else:
        print(-1)


