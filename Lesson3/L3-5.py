def summa_num():
	summa = 0
	while True:
		list = input("Введите числа через пробел или знак $ для выхода из программы:\n").split()
		for i in list:
			try:
				if i == "$":
					return print(f"Сумма чисел равна: {summa}. Выполнен выход.")
				else:
					summa +=int(i)
			except Exception as er:
				print(f"Были введены не только цифры")
		print(f"Сумма чисел равна: {summa}")

summa_num()