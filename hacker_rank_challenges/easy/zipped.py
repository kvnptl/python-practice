

# Sample Code

# >>> print zip([1,2,3,4,5,6],'Hacker')
# [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
# >>> 
# >>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
# [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
# >>> 
# >>> A = [1,2,3]
# >>> B = [6,5,4]
# >>> C = [7,8,9]
# >>> X = [A] + [B] + [C]
# >>> 
# >>> print zip(*X)
# [(1, 6, 7), (2, 5, 8), (3, 4, 9)]

ip = [int(i) for i in input().split()]

subjects_list = []

for i in range(ip[1]):
    subjects_list.append([float(j) for j in input().split()])

for i in zip(*subjects_list):
    print(sum(i)/len(i))
    