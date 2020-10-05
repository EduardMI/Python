def my_func(x, y):
	"""функция возведения в степень

	:param x: число
	:param y: степень возведения
	:return:
	"""
	return x ** y

def my_func_2(x,y):
	"""функция возведения в отрицательную степень через цикл

	:param x: число
	:param y: степень возведения
	:return:
	"""
	n = x
	for i in range(1, abs(y)):
		n = n * x
	return 1 / n

x = float(input("Введите число: "))
y = int(input("Введите отрицательную степень в которое необходимо возвести число: "))

print(my_func_2(x, y))
print(my_func(x, y))