'''Closures Examples with Python
Special thanks to Corey Schafer (it was based on his video)

More in: 
https://www.youtube.com/watch?v=swU3c34d2NQ&feature=iv&src_vid=FsAPt_9Bf3U&annotation_id=video%3A9fbfd6c3-4a93-4851-8b79-c97fa98dca18

'''

def outer_func(msg='Hi!'):
	def inner_func(message=msg):
		print(message)
	return inner_func #Just return the inner function.

f = outer_func()
f()



#Creates a "print" which prints the result and the parameters from a function

def printer(func):

	def printer_f(*args): #Here we will get all func parameters
		print('Function Name: {} / Parameters: {}'.format(func.__name__, *args))
		print(func(*args)) #Here, we execute the default function operation along with its parameteres.
	return printer_f #Return the high-order function object printer_f, then we can assign it to a variable.

def foo(name):
	return name + ' foo'

def bar(name):
	return name + ' bar'

'''Here we are "saving" the function outside the environment. So when calling the 
printer_foo, whatever parameters you pass to the function, it's going to keep "saved" the function
foo. '''
printer_foo = printer(foo) 

printer_bar = printer(bar)

printer_foo('Henrique')
printer_foo('Any Name')

printer_bar('Henrique')
'''Again, whatever string you pass, it will always execute the function bar, which again
   comes from the outer function (in this case, the printer function''' 
printer_bar('Any Name') 

