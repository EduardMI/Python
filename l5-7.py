import json

with open("l5-7.txt", "r") as f_obj:
	dict = {}
	dict_profit = {}
	count = 0
	total_income = 0
	for el in f_obj:
		var_list = el.split()
		income = float(var_list[2]) - float(var_list[3])
		if income > 0:
			count += 1
			total_income += income
		dict[var_list[0]] = income
	dict_profit["average_profit"] = total_income / count
	total_list = [dict, dict_profit]

with open("l5-7.json", "w") as j_file:
	json.dump(total_list, j_file)

# with open("l5-7.json", "r") as j_file_r:
# 	j_str = json.load(j_file_r)
# 	print(j_str)