if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    arry = []
    final_arry = []

    # Using nested for loops
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             arry.append([i, j, k])

    # for a in range(len(arry)):
    #     if (arry[a][0] + arry[a][1] + arry[a][2]) != n:
    #         final_arry.append(arry[a])

    # Using list comprehension
    arry = [[i, j, k] for i in range(x+1)
            for j in range(y+1) for k in range(z+1)]

    final_arry = [arry[a] for a in range(len(arry)) if (
        arry[a][0] + arry[a][1] + arry[a][2]) != n]

    print("ok")
