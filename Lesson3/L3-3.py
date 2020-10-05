def my_func(a, b, c):
	"""Нахождение суммы наибольших 2х чисел из 3х


	:param a:
	:param b:
	:param c:
	:return:
	"""
	result = [a, b, c]
	min_num = min(a, b ,c)
	result.remove(min_num)
	return print(f"Сумма наибольших 2-х из введеных чисел равна {sum(result)}")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

my_func(a, b, c)