from itertools import groupby

ip_string = input()

l = []
for i, g in groupby(ip_string):
    l.append(str((len(list(g)), int(i))))

print(" ".join(l))
