'''Decorators permits we add easily functionalities to existing functions.
by adding that functionality inside that wrapper without modifyingare function that takes an functionality, without alternating the code.

Special thanks to Corey Schafer
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



def display_bar():
	print('Bar')

@decorator_f
def display_info(name, age):
	print('{0}: {1}'.format(name, age))

#display()
#display()
#display_info('Henrique', 24)


'''You can use classes instead of function decorators (however, it's not used frequently
. So, let's do it based on the example
above	
 Follow this steps:
 1- Create a new class (Decorator);
 2- As above, we needed to pass the wrapped function as a parameter to the decorator. We need to do
 	the same for the class to __init__ built-in method;. This way, we're attaching the 
 	original function to a reference in the class;
 3- We can implement __call__ method which behaves like a "shortcut" when calling the 
 	object instance. For instance, we will pass *args, **kwargs as parameters, since we have to pass the parameters defined in the wrapped
 	function to __call__ function, ;
 4- At the end of __call__ method, we have to return the attribute which represents
    the wrapped_function. '''
  
class Decorator:

	def __init__(self, wrapped_function):
		self.wrapped_f = wrapped_function

	def __call__(*args, **kwargs):
		print('Method {} executing...'.format(self.wrapped.__name__))
		return self.wrapped_f(*args, **kwargs)


'''Below there are other more practical examples of decorators: '''



def logger(wrapped_f):
	"""Decorator which provides to the wrapped function display logging information."""
	import logging
	logging.basicConfig(fileName='{}.log'.format(wrapped_f.__name__), level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info('Function: {}'.format(wrapped_f.__name__))
		return wrapped_f(*args, **kwargs)
	return wrapper	


def timer(wrapped_f):
	"""Decorator which provides to the wrapped function shows the time running a callable."""
	import time

	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = wrapped_f(*args, **kwargs)
		t2 = time.time() - t1
		print('{} performed in: {} secs'.format(wrapped_f.__name__, t2))
		return result
	return wrapper

@logger
def display_foo():
	print('Foo')

display_foo()



