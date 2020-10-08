list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list if list.count(el) < 2]

# for i in list:
# 	if list.count(i) < 2:
# 		new_list.append(i)

print(list)
print(new_list)