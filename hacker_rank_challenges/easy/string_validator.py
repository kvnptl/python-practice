if __name__ == '__main__':
    s = input()
    lst = [i.isalnum() for i in s]
    print(any(lst))
    
    lst = [i.isalpha() for i in s]
    print(any(lst))
        
    lst = [i.isdigit() for i in s]
    print(any(lst))
        
    lst = [i.islower() for i in s]
    print(any(lst))
    
    lst = [i.isupper() for i in s]
    print(any(lst))
        
