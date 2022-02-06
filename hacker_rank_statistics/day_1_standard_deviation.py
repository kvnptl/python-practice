#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):

    # Print your answers to 1 decimal place within this function
    # mean
    sum_arr = 0
    for i in arr:
        sum_arr += i
    mean = sum_arr/len(arr)
    # print("{:.1f}".format(mean))
    squared_dist_from_mean_list = [(arr[i]-mean)**2 for i in range(len(arr))]
    std = (sum(squared_dist_from_mean_list)/len(arr))**(0.5)
    print(round(std, 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
