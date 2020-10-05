def defin(name, family, b_day, city, email, tel_number):
	return " ".join([name, family, b_day, city, email, tel_number])

name = input("Введите имя: ")
family = input("Введите фамилию: ")
b_day = input("Введите дату вашего рождения: ")
city = input("Введите город проживания: ")
email = input("Введите адрес электронной почты: ")
tel_number = input("Введите номер телефона: ")

print(defin(name, family, b_day, city, email, tel_number))
