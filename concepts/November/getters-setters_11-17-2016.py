"""
	Property decorators: 

	1. @property - It allows to access the attribute along with its value. 
	  Syntax-Usage (by the client): obj.foo

	  Syntax to Create : 

	    @property
	    def foo(self):
	   	    return self.property



	2. @[property-name].setter = It allows to pass values to a property.

		@foo.setter:
			def foo(self, arg):
				self.property = arg

	  Syntax-Usage (by the client):[object].[attribute] = [value]  -  obj.foo = 'foo'
	@[property-name].deleter = It "deletes" / "erases" the attributes from the class. 

		@[property-name].setter = It allows to attribute values to a property. 

		@foo.deleter:
			def foo(self):
				self.property = None



	  Syntax Usage (by the client):
	      del obj.foo
"""
class EmployeeEmail:

	def __init__(self, first, last, domain='foo.com'):
		""""""
		self.first = first
		self.last = last
		self.domain = domain
	
	@property
	def email(self):
		"""Method with a decorator @property. It returns the email 
		from a employee created based
		on the """
		return '@'.join(['.'.join([self.first, self.last]), self.domain])


	@property
	def fullname(self):
		""""Another function with @property decorator. It returns both the first and last 
		name with the first letter capitalized (upper case)."""
		return ' '.join([self.first.capitalize(), self.last.capitalize()])

	@fullname.setter
	def fullname(self, name):
		"""Setter for property that redefines both first, last and domain. 
			Notice that we're using a decorator for the 'fullname' attribute. You can use
			it for attributes decorated by @property (For test and curiosity purposes, remove 
			the @property decorator above and check what happens by building it ;) ).

		"""
		self.first, self.last = name.split()

	@fullname.deleter
	def fullname(self, name):
		"""Deleter for property that redefines both first, last and domain. 
			Notice that we're using a decorator for the 'fullname' attribute. You can use
			it for attributes decorated by @property_name.setter (For test and curiosity purposes, remove 
			the @property_name.setter decorator above and check what happens by building it ;) ).

		"""
		print('Erasing names... 1 sec please.')
		self.first = ''
		self.last = ''
		self.domain = ''



if __name__ == '__main__':
	#Initializes a new EmployeeEmail instance.
	e = EmployeeEmail('henrique', 'albor')
	#Access both @property decorated classes email and fullname.
	print(e.email, e.fullname)
	#Access decorator @fullname.setter to alter values.
	e.fullname = 'foo bar' 
	print(e.email) #printing the email after changes.
	print(e.fullname) #printing the fullname after changes.
