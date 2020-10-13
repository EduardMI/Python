list = []
dict = {}

with open("l5-3.txt", encoding="UTF-8") as f_obj:
	for line in f_obj:
		list = line.split()
		dict[list[0]] = float(list[1])

low_pay = [key for key in dict if dict[key] < 20000]

print(f"Cотрудникик которые имеют зарплату ниже 20000: {', '.join(low_pay)}\n"
	  f"Среднняя зарплата сотрудников: {sum(dict.values()) / len(dict):.2f}")