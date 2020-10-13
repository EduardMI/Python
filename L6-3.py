class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage,
					   "bonus": bonus}


class Position(Worker):
	def get_full_name(self):
		return f"{self.surname} {self.name}"

	def get_total_income(self):
		return self._income["wage"] + self._income["bonus"]


if __name__ == "__main__":
	pos = Position("Ivan", "Ivanov", "boss", 100, 30)
	print(pos.get_full_name())
	print(pos.get_total_income())
	print(pos.name, pos.surname, pos.position, pos._income)