def division(arg1, arg2):
	""" функция деления чисел

	:param arg1: делимое
	:param arg2: делитель
	:return:
	"""
	return arg1 / arg2

num1 = input("Ввведите первое число: ")
num2 = input("Ввведите второе число: ")

try:
	num1 = float(num1)
	num2 = float(num2)
	# result = division(num1, num2)
	print(f"Результатом деления {num1} на {num2} является {division(num1, num2):.2f}")
except ZeroDivisionError:
	print("На ноль делить нельзя!")
except Exception as error:
	print("Не корректный ввод данных")