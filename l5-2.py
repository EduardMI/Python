with open("l5-2.txt", "r") as f_obj:
    lines = 0
    for line in f_obj:
        if line.split():
            lines +=1
            print(f'В {lines}-ой строке слов: {len(line.split())}')