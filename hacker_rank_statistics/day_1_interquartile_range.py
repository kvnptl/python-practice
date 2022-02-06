#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    if len(values) == len(freqs):
        new_list = []
        for i in range(len(values)):
            for _ in range(freqs[i]):
                new_list.append(values[i])

    new_list = sorted(new_list)
    if len(new_list) % 2 == 0:
        q2 = (new_list[len(new_list)//2 - 1] + new_list[len(new_list)//2])//2

        q1_list = new_list[:len(new_list)//2]
        if len(q1_list) % 2 != 0:
            q1 = q1_list[(len(q1_list)//2)]
        else:
            q1 = (q1_list[len(q1_list)//2 - 1] + q1_list[len(q1_list)//2])//2

        q3_list = new_list[(len(new_list)//2):]
        if len(q3_list) % 2 != 0:
            q3 = q3_list[(len(q3_list)//2)]
        else:
            q3 = (q3_list[len(q3_list)//2 - 1] + q3_list[len(q3_list)//2])//2

    elif len(new_list) % 2 != 0:
        q2 = new_list[(len(new_list)//2)]

        q1_list = new_list[:(len(new_list)//2)]
        if len(q1_list) % 2 != 0:
            q1 = q1_list[(len(q1_list)//2)]
        else:
            q1 = (q1_list[len(q1_list)//2 - 1] + q1_list[len(q1_list)//2])//2

        q3_list = new_list[(len(new_list)//2)+1:]
        if len(q3_list) % 2 != 0:
            q3 = q3_list[(len(q3_list)//2)]
        else:
            q3 = (q3_list[len(q3_list)//2 - 1] + q3_list[len(q3_list)//2])//2

    # return [round(q1, 1), round(q2, 1), round(q3, 1)]
    print("{:.1f}".format(q3-q1))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
