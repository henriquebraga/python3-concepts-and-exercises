'''Decorators permits we add easily functionalities to existing functions.
by adding that functionality inside that wrapper without modifyingare function that takes an functionality, without alternating the code.

'''

'''Below there's an example reviewing closures (from day 10/11) '''

# def decorator_f(original_function):
# 	def wrapper_f():
# 		foo()
# 	return wrapper_f

# def foo():
# 	print('foo')

#def decorator

def decorator_f(f):
	print('''Wrapper executing from the outside. 
		(when we call the function decorator_f (outer function)
		After that we will execute function "{}", which
		is the wrapped function.'''.format(f.__name__))
	
	def decorated_f(*args):
		return f(*args)
	return decorated_f

@decorator_f
def display():
	print('Hi there!')

def display_foo():
	print('Foo')

def display_bar():
	print('Bar')

@decorator_f
def display_info(name, age):
	print('{0}: {1}'.format(name, age))

display()
display()
display_info('Henrique', 24)
#decorated_display = decorator_f(display)
#decorated_display()
#decorated_display()
print('\n')

# foo_display = decorator_f(display_foo)
# foo_display()
# bar_display = decorator_f(display_bar)
# bar_display()








