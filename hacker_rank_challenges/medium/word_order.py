# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

words = {}
for _ in range(n):
    s = input()
    if s not in words.keys():
        words[s] = 1
    else:
        words[s] += 1

print(len(words.keys()))

[print(i, end=' ') for i in list(words.values())]
