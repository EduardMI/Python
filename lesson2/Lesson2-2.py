list1 = [1, 2, 3, 4, 5]
list2 = []
list3 = [1]
list4 = [1, 2, 3, 4, 5, 6]

def enum(list):
    j = 0
    for i in range(int(len(list)/2)):
        list[j], list[j + 1] = list[j + 1], list[j]
        j += 2


enum(list1)
enum(list2)
enum(list3)
enum(list4)
print(list1)
print(list2)
print(list3)
print(list4)