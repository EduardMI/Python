string = input("Введите строку из нескольких слов разделяя слова пробелами: ")

list = string.split()

for ind, el in enumerate (list, 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind, el)
