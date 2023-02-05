
'''
Learn more about @decorator in Python: https://youtu.be/r7Dtus7N4pI 
Learn about *args, **kwargs: https://youtu.be/GdSJAZDsCZA 
'''

def wrapper(func):
    def fun(l):
        # complete the function
        ll = ['+91 ' + i[-10:-5] + ' ' + i[-5:] for i in l]
        func(ll)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    la = [input() for _ in range(int(input()))]
    sort_phone(la) 

