class Human():
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

class Boy(Human):
	pass

Raj = Boy("Raj", "Sharma", 50)

print(Raj.first)
print(Raj.last)
print(Raj.age)
