from time import sleep


class TrafficLight:
	def __init__(self):
		self._color = ["Красный", "Желтый", "Зеленый"]

	def switch(self):
		i = 0
		while i < 3:
			print(self._color[i])
			if i == 0:
				sleep(7)
			elif i == 1:
				sleep(2)
			elif i == 2:
				sleep(10)
			i += 1


if __name__ == '__main__':
	TrafficLight = TrafficLight()
	TrafficLight.switch()
