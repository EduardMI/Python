def fact(x):
	factor = 1
	for i in range(1, n+1):
		factor = factor * i
		yield factor

n = 5

for el in fact(n):
	print(el)
