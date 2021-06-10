class Animal:
	name = None
	size = None

	def __init__(self, size, name):
		self.size = size
		self.name = name

	def printName(self):
		print(self.name)

dog = Animal(12, "Lulu")
dog.printName()