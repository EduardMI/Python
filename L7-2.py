class Clothes:
	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.value = ""

	def __add__(self, other):
		return str(f"Общая площадь ткани: {(self.calc + other.calc):.2f}")

	def __str__(self):
		return f"{self.name}: {self.value} {self.size}"

	@property
	def calc(self):
		return self.size


class Coat(Clothes):
	def __init__(self, name, size):
		super().__init__(name, size)
		self.value = "размер"

	@property
	def calc(self):
		return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
	def __init__(self, name, size):
		super().__init__(name, size)
		self.value = "рост"

	@property
	def calc(self):
		return round(self.size * 2 + 0.3, 2)


if __name__ == "__main__":
	sample_1 = Coat("Пальто", 43)
	sample_2 = Suit("Костюм", 1.95)
	print(sample_1)
	print(sample_2)
	print(sample_1.calc)
	print(sample_2.calc)
	total = sample_1 + sample_2
	print(total)
