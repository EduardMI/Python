bad_list = [":", "(л)", "(лаб)", "(пр)", "—", "."]
dict = {}
def add_dictionary(el):
	""""Добавление значений в словарь из строк с удалением посторонних знаков
	"""
	for i in bad_list:
		el = el.replace(i, "")
	var_list = el.split() # имеет смысл убрать эту строку и заменить везде переменную var_list на el.split()???
	int_list = [int(i) for i in var_list[1:]]
	dict[var_list[0]] = sum(int_list)


with open("l5-6.txt", encoding="UTF-8") as f_obj:
	for el in f_obj:
		add_dictionary(el)

print(dict)
