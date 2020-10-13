dict = {"One": " Один",
		"Two": "Два",
		"Three": "Три",
		"Four": "Четыре"}
list = []
with open("l5-4.txt", encoding="UTF-8") as f_obj, open("l5-4-2.txt", "w", encoding="UTF-8") as f_test:
	for el in f_obj:
		el.strip()
		list = el.split()
		if list[0] in dict:
			list[0] = dict[list[0]]
			print(f"{''.join(list).strip()}", file=f_test)
		# ''.join(list).strip() - добавил strip, так как в первой строке появлялся пробел первым символом
 