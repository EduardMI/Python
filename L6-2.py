from functools import reduce


class Road:
	def __init__(self, length, width):
		self._lenght = length
		self._width = width
		_density = 25
		_layer = 5
		self._list = [self._lenght, self._width, _density, _layer]

	def calculation(self):
		return print(f"{reduce(lambda x, y: x * y, self._list) / 1000:.0f} тонн")


if __name__ == '__main__':
	calc = Road(5000, 20)
	calc.calculation()
