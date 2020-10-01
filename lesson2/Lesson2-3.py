list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
dict = {"зима": [1, 2, 12],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11]}

try:
    number = int(input("Введите номер месяца: "))
    if number < 1 or number > 12:
        raise Exception()
    print(f"{number}-й месяц относится к следующему времени года: {list[number - 1]}")

    for i in dict:
        if number in dict[i]:
            print(f"{number}-й месяц относится к следующему времени года: {i}")

except Exception as message:
    print("Вы неверно ввели номер месяца.")
