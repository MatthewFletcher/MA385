import math


def pxeqk(l,k):
	pxeqk = (l**k)/math.factorial(k) * math.exp(-l)
	return pxeqk


sum = 0

l = float(input("Enter lambda> "))
for x in range(0,5):
	print("Finding probability x = ",x)
	sum+=pxeqk(l,x)

print(sum)