class Dog:
	def __init__(self,name):
		self.name = name
		self.tricks = []

	def add_trick(self,trick):
		self.tricks.append(trick)


p1 = Dog("boby")
p2 = Dog("rambo")

p1.add_trick("volteos")
p2.add_trick("mordida")

print(p1.tricks)
print(p2.tricks)
