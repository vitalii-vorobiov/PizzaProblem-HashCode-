class Pizza:
	def __init__(self):
		self.data = []
		self.rows = 0
		self.columns = 0
		self.min_ingredient = 0
		self.max_cells = 0

	def read_data(self, filename):
		"""
		Mushroom = 0
		Tomato = 1
		"""
		with open(filename, 'r') as f:
			self.rows, self.columns, self.min_ingredient, self.max_cells = f.readline().strip().split()

			i = 0
			for line in f.readlines():
				temp = []
				for letter in line.strip():
					temp.append(letter)

				self.data.append([])

				for item in temp:
					if item == "T":
						self.data[i].append(1)
					else:
						self.data[i].append(0)
				i += 1


	def slice(self):
		pass


if __name__ == "__main__":

	pizza = Pizza()
	pizza.read_data("a_example.in")

	print(pizza.data)