# Author: Ryan (AMDG) 10/14/21

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))

# class solution
# distance = (((x2 - x1) ** 2) + ((y2 -y1) ** 2)) ** (1/2)

cord_1 = (x2 - x1) ** 2
cord_2 = (y2 - y1) ** 2

d = cord_1 + cord_2 

distance = d ** (1/2)
print("distance is: ", str(distance))
