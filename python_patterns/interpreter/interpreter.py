#-*- coding: utf-8 -*-


class Operation:

	def __init__(self, left_expression, right_expression):
		self._left_expr = left_expression
		self._right_expr = right_expression


class Substraction:
	
	def __init__(self, left_expression, right_expression):
		self._left_expr = left_expression
		self._right_expr = right_expression

	def __call__(self):
		return self._left_expr() - self._right_expr()


class Add:
	
	def __init__(self, left_expression, right_expression):
		self._left_expr = left_expression
		self._right_expr = right_expression

	def __call__(self):
		return self._left_expr() + self._right_expr()

class Multiplication:
	
	def __init__(self, left_expression, right_expression):
		self._left_expr = left_expression
		self._right_expr = right_expression

	def __call__(self):
		return self._left_expr() - self._right_expr()

class Number:
	'''Caso base para recursão.'''
	def __init__(self, num):
		self._num = num

	def __call__(self):
		return self._num

if __name__ == '__main__':

	number_5 = Number(5)
	number_3 = Number(3)
	assert number_5() == 5
	assert number_3() == 3

	sub_expression = Substraction(Number(5), Number(3))
	sub_expression_2 = Substraction(Number(1), Number(4))
	assert sub_expression() == 2
	assert sub_expression_2() == - 3

	sum_expression = Add(Number(4), Number(2))
	sum_expression_2 = Add(Number(-3), Number(-2))
	assert sum_expression() == 6
	assert sum_expression_2() == -5

	left_expression = Add(Number(5), Number(3))
	right_expression = Substraction(Number(3), Number(1))
	composed_expression = Add(left_expression, right_expression)
	assert composed_expression() == 10


