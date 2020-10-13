with open("l5-5.txt", "w") as f_obj:
	print(input("Введите числа через пробел: "), file=f_obj)
with open("l5-5.txt", "r") as file:
	for el in file:
		int_list = [int(x) for x in el.split()]
		print(sum(int_list))
