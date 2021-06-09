import numpy

coeff = [float(num) for num in input().split()]
x = int(input())

print(numpy.polyval(coeff, x))