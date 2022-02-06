#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        q2 = (arr[len(arr)//2 - 1] + arr[len(arr)//2])//2

        q1_list = arr[:len(arr)//2]
        if len(q1_list) % 2 != 0:
            q1 = q1_list[(len(q1_list)//2)]
        else:
            q1 = (q1_list[len(q1_list)//2 - 1] + q1_list[len(q1_list)//2])//2

        q3_list = arr[(len(arr)//2):]
        if len(q3_list) % 2 != 0:
            q3 = q3_list[(len(q3_list)//2)]
        else:
            q3 = (q3_list[len(q3_list)//2 - 1] + q3_list[len(q3_list)//2])//2

    elif len(arr) % 2 != 0:
        q2 = arr[(len(arr)//2)]

        q1_list = arr[:(len(arr)//2)]
        if len(q1_list) % 2 != 0:
            q1 = q1_list[(len(q1_list)//2)]
        else:
            q1 = (q1_list[len(q1_list)//2 - 1] + q1_list[len(q1_list)//2])//2

        q3_list = arr[(len(arr)//2)+1:]
        if len(q3_list) % 2 != 0:
            q3 = q3_list[(len(q3_list)//2)]
        else:
            q3 = (q3_list[len(q3_list)//2 - 1] + q3_list[len(q3_list)//2])//2

    return [round(q1, 1), round(q2, 1), round(q3, 1)]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
