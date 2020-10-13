class Stationery:
	def __init__(self, title):
		self.title = title

	def draw(self):
		print(f"Запуск отрисовки.")


class Pen(Stationery):
	def draw(self):
		print(f"Запуск отрисовки ручкой.")


class Pencil(Stationery):
	def draw(self):
		print(f"Запуск отрисовки карандашом.")


class Handle(Stationery):
	def draw(self):
		print(f"Запуск отрисовки маркером.")


if __name__ == '__main__':
	draw = Stationery("рисование")
	draw.draw()
	pen = Pen("Ручка")
	pen.draw()
	pencil = Pencil("Карандаш")
	pencil.draw()
	handle = Pen("Маркер")
	handle.draw()
