# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

ip = int(input())

ord_dict = OrderedDict()

for i in range(ip):
    tmp = input().split()
    item_name, price = " ".join(tmp[:-1]), int(tmp[-1])
    
    if item_name in ord_dict:
        ord_dict[item_name] += price
    else:
        ord_dict[item_name] = price

print("\n".join([" ".join([k, str(v)]) for k, v in ord_dict.items()]))
