from collections import Counter

x = int(input())
shoe_size_str = input().split()
shoe_size_list = [int(i) for i in shoe_size_str]

stock_list = Counter(shoe_size_list)

total_customers = int(input())

customer_order = []
earned_money = 0

for i in range(total_customers):
    shoe_size, shoe_price = input().split()
    
    if int(shoe_size) in list(stock_list.keys()):
        if stock_list[int(shoe_size)] > 0:
            stock_list[int(shoe_size)]-=1
            earned_money+=int(shoe_price)

print(earned_money)
