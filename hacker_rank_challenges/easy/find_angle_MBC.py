import math

ab = input()
bc = input()

# apply pythagorean theorem
ac = (float(ab)**2 + float(bc)**2)**0.5

# fina the angle
angle = math.atan(float(ab)/float(bc))

# convert the angle to degrees
angle = angle * (180/math.pi)

print(str(round(angle)) + chr(176))