chek = False
while not chek:
    str = input("Введите текст:\n (для завершения ввода нажмите Enter)\n")
    if bool(str) == True:
        with open("l5-1.txt", "a", encoding="UTF-8") as f_obj:
            f_obj.write(f"{str}\n")
    else:
        chek = True
