from sys import argv

name, time, rate, bonus = argv
# time = int(time)
# rate = int(rate)
# bonus = int(bonus)

def income(time, rate, bonus):
	try:
		time = int(time)
		rate = int(rate)
		bonus = int(bonus)
		res = time * rate + bonus
		return print(f"заработная плата составляет: {res}.")
	except ValueError:
		print("Были введены не только цифры")

income(time, rate, bonus)