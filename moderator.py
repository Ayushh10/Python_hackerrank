# A User class with both a class attribute
class User:

	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users."

	@classmethod
	def from_string(cls):
		first, last, age = data_str.split(" ")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self): 
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

class Moderator(User):
	def __init__(self, first, last,age, community):
		super().__init__(first, last, age)
		self.community = community

    # def post_deleted(self):
    # 	return f"{self.full_name()} deleted your post from {self.community} community"


print(User.display_active_users())
u1 = User("Tom", "Garcia", 43)
print(User.display_active_users())
Jack = Moderator("Jack", "Sparrow", 40, "BLACKPEARL")
print(User.display_active_users())
