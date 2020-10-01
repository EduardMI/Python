my_list = [7, 5, 3, 3, 2]

numb = int(input())

# my_list.append(numb)
# my_list.sort()
# my_list.reverse()

for i in reversed(my_list):
	max_list = max(my_list)
	if numb > max_list:
		my_list.insert(0, numb)
		break
	elif numb <= i:
		n = my_list.index(i) + 1
		my_list.insert(n, numb)
		break

print(my_list)