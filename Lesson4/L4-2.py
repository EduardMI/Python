list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list[i +1] for i in range(len(list) - 1) if list[i] < list[i +1]]

print(list)
print(new_list)
