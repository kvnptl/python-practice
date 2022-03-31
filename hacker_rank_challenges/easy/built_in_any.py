# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# lst = input().split()

#my poor answer
# flag = 0
# f = 0
# for i in lst:
#     if i[0] == '-':
#         print("False")
#         f = 1
#         break

# if f != 1:
#     for i in lst:
#         if len(i)%2 == 0:
#             l = len(i)//2
#             for j in range(l):
#                 if i[j] == i[-j-1]:
#                     if j == l-1:
#                         print("True")
#                         flag = 1
#                         break
#             if flag == 1:
#                 break
        
#         else:
#             l = round(len(i)/2)
#             if l==0: 
#                 print("True")
#                 flag = 1
#                 break
#             for k in range(l):
#                 if i[k] == i[-k-1]:
#                     if k == l-1:
#                         print("True")
#                         flag = 1
#                         break

#             if flag == 1:
#                 break

#     if flag == 0:
#         print("False")    
        
# community best answer

n = int(input())
lst = input().split()
print( all([int(i)>0 for i in lst]) and any([j == j[::-1] for j in lst]))