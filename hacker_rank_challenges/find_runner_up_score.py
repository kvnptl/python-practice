if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr_set = set(arr)
    m = max(arr_set)
    arr_set.remove(m)
    print(max(arr_set))
