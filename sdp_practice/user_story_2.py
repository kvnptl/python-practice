import numpy as np
import pandas as pd
import math

# x_m = float(input())

# x_m_list = [0.2, 6, 1, 2, 3, 4, 5]

x_m_list = np.linspace(0.0, 6.28, num=64)

pi = 3.14

# x_d = math.fmod(2.10 + pi), 2*pi)
x_d = math.fmod(3.47 + pi, 2*pi)
# x_d = math.fmod(2.94 + pi), 2*pi)
# x_d = math.fmod(0.60 + pi), 2*pi)



print("x_d_1: {} to {}".format(x_d, math.fmod(x_d + 3.14, 6.28)))

direction_list = []

if x_d > 3.14:
    x_d = x_d - 2*3.14

    for x_m in x_m_list:

        if x_m > 3.14:
            x_m = x_m - 2*3.14

            if x_m > x_d:
                direction_list.append("Clockwise")
                # print("Clockwise")
            else:
                direction_list.append("Anticlockwise")
                # print("Counterclockwise")

        elif 0 <= x_m <= 3.14:
            if x_d < x_m < x_d + 3.14:
                direction_list.append("Clockwise")
                # print("Clockwise")
            else:
                direction_list.append("Anticlockwise")
                # print("Counterclockwise")
else:

    for x_m in x_m_list:    

        if x_m > 3.14:
            x_m = x_m - 2*3.14

            if x_m < x_d - 3.14:
                direction_list.append("Clockwise")
                # print("Clockwise")
            else:
                direction_list.append("Anticlockwise")
                # print("Counterclockwise")

        elif 0 <= x_m <= 3.14:
            if x_d < x_m:
                direction_list.append("Clockwise")
                # print("Clockwise")
            else:
                direction_list.append("Anticlockwise")
                # print("Counterclockwise")


data = { 'Measurement': x_m_list, 'Direction': direction_list }

pd_data = pd.DataFrame.from_dict(data, orient='index')
pd_data = pd_data.transpose()
pd_data.to_csv('output.csv', index=None)