'''

Sample Input:
Sorting1234

Sample Output: 
ginortS1324

'''

ip_str = input()

sort_ip = sorted(ip_str)

lower_case = []
upper_case = []
odd_numbers = []
even_numbers = []

for i in range(len(ip_str)):
    if ip_str[i].islower():
        lower_case.append(ip_str[i])
    elif ip_str[i].isupper():
        upper_case.append(ip_str[i])
    elif ip_str[i].isdigit():
        if int(ip_str[i]) % 2 == 0:
            even_numbers.append(ip_str[i])
        else:
            odd_numbers.append(ip_str[i])

print(''.join(''.join(sorted(lower_case)) + ''.join(sorted(upper_case)) + ''.join(sorted(odd_numbers)) + ''.join(sorted(even_numbers))))