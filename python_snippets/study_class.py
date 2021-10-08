class Student: 

	def __init__(self):
		self.name = 'Valdir'

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"Person: {self.name}, {self.age} years old."

	def __repr__(self):
		return f"<Person('{self.name}', {self.age})>"

class Book:

	TYPES = ('hardcover', 'paperback')

	def __init__(self, name, book_type, weight):
		self.name = name
		self.book_type = book_type
		self.weight = weight

	def __repr__(self):
		return f"<Book {self.name}, {self.book_type}, {self.weight}g>"

	@classmethod
	def hardcover(cls, name, page_weight):
		return cls(name, cls.TYPES[0], page_weight + 100)

	@classmethod
	def paperback(cls, name, page_weight):
		return cls(name, cls.TYPES[1], page_weight)

	
# book = Book('Happy Poter', 'hard cover', 140)
# book = Book.hardcover('Harry Potter', 1200)
book = Book.paperback('Harry Potter', 1200)

print(book)



# print(Book.TYPES)

# valdir = Person('Valdir', age=35)

# print(valdir)


import sys
print(sys.path)
