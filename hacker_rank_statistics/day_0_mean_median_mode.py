
'''
Input Format

The first line contains an integer, N, the number of elements in the array.
The second line contains N space-separated integers that describe the array's elements.

Output Format

Print 3 lines of output in the following order:
Print the mean on the first line to a scale of 1 decimal place (i.e., 12.3, 7.0).
Print the median on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
Print the mode on a new line. If more than one such value exists, print the numerically smallest one.
'''

# Enter number of integers
from collections import Counter
n = int(input())
# Enter integers
x = input().split(" ")
x = x[:n]
# convert string list to int list
x = [int(i) for i in x]

# mean
sum = 0
for i in x:
    sum += i
mean = sum/n
print("{:.1f}".format(mean))

# median
x = sorted(x)
if n % 2 == 0:
    median = (x[n//2 - 1]+x[n//2])/2
elif n % 2 != 0:
    median = x[(n//2)]
else:
    median = 0
print("{:.1f}".format(median))

# mode
c = Counter(x)
mode = c.most_common(1)[0][0]
print("{:.1f}".format(mode))
