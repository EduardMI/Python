# переменная direction при наличии только класса Car работала как nonlocal переменная
# в функции turn и была обьявлена внутри класса,
# а после добавления других классов перестала, выделил как глобал. Подскажите почему? =)

from random import choice

direction = ["направо", "налево", "вперед", "в обратном направлении"]


class Car:
	# direction = ["направо", "налево", "вперед", "в обратном направлении"]

	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		return print(f"Машина {self.name} поехала")

	def stop(self):
		return print(f"Машина {self.name} остановилась")

	def turn(self):
		# nonlocal direction
		global direction
		return print(f"Машина {self.name} поехала {choice(direction)}")

	def show_speed(self):
		return print(f"Скорость машины {self.name}: {self.speed}")


class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			return print(f"Машина {self.name} превысила скорость")
		else:
			return print(f"Скорость машины {self.name}: {self.speed}")


class SportCar(Car):
	pass


class PoliceCar(Car):
	def police(self):
		if self.is_police:
			return print(f"{self.name} это полицейская машина")
		else:
			return print(f"{self.name} это не полицейская машина")


class WorkCar(PoliceCar):
	def show_speed(self):
		if self.speed > 40:
			return print(f"Машина {self.name} превысила скорость")
		else:
			return print(f"Скорость машины {self.name}: {self.speed}")


if __name__ == "__main__":
	car = Car(60, "red", "Ford", None)
	lada = TownCar(80, "blue", "Lada", None)
	niva = TownCar(55, "blue", "Niva", None)
	police = PoliceCar(100, "black", "Nissan", True)
	volga = WorkCar(40, "white", "Volga", None)
	car.go()
	car.turn()
	car.stop()
	car.show_speed()
	lada.show_speed()
	niva.show_speed()
	volga.show_speed()
	police.police()
	volga.police()  # не работает если порядок наследования (Car, PoliceCar), почему?
