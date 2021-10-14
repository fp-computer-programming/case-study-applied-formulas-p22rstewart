# Author: Ryan (AMDG) 10/14/21

p = int(input("Enter the principal investment: "))
r = float(input("Enter the annual intrest rate (as a decimal): "))
#n = int(input("Enter the # of times that the intrest is compounded per unit: "))
t = int(input("Enter the amount of time that the money is invested (in years): "))

n = 12
r /= 100

a = p * ((1 + (r / n)) ** (n * t))

print("In " + str(t) + "Years, the account will contain  S" + str(a))
