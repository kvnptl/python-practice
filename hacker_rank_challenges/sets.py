# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split(" ")

array_n = input().split(" ")
array_n = array_n[:int(n)]

elem_a = input().split(" ")
elem_b = input().split(" ")

elem_a = elem_a[:int(m)]
elem_b = elem_b[:int(m)]

elem_a = set(elem_a)
elem_b = set(elem_b)

happy = 0

for i in array_n:
    if i in elem_a:
        happy += 1
    elif i in elem_b:
        happy -= 1

print(happy)
