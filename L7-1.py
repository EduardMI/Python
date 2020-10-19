class Matrix:
	def __init__(self, name, array):
		self.name = name
		self.array = array


	def __add__(self, other):
		return Matrix(
			name=f"{self.name}_{other.name}",
			array=self.add_array(self.array, other.array)
		)


	def add_array(self,temp_1, temp_2):
		for i in range(len(temp_1)):
			for j in range(len(temp_1[i])):
				temp_1[i][j] = temp_1[i][j] + temp_2[i][j]
		return temp_1


	def __str__(self):
		return str("\n".join([("\t".join([str(j) for j in i])) for i in self.array]))


if __name__ == '__main__':
	matr_1 = Matrix("One", [[1, 1, 1], [1, 1, 0]])
	matr_2 = Matrix("Two", [[2, 2, 2], [2, 2, 2]])
	# print(matr_1)
	# print(matr_2)
	matr_3 = matr_1 + matr_2
	print(matr_3.name)
	print(matr_3.array)
	print(matr_3)
