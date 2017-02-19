#-*- coding: utf-8 -*-


class Operation(object):

	def __init__(self, left_expression, right_expression):
		self._left_expr = left_expression
		self._right_expr = right_expression


class Substraction(Operation):

	def accept(self, visitor):
		return visitor.visit_substraction(self)

	def __init__(self, left_expression, right_expression):
		super(Substraction, self).__init__(left_expression, right_expression)

	def __call__(self):
		return self._left_expr() - self._right_expr()


class Add(Operation):

	def accept(self, visitor):
		return visitor.visit_add(self)
	
	def __init__(self, left_expression, right_expression):
		super(Add, self).__init__(left_expression, right_expression)

	def __call__(self):
		return self._left_expr() + self._right_expr()


class Multiplication(Operation):
	
	def __init__(self, left_expression, right_expression):
		super(Add, self).__init__(left_expression, right_expression)

	def __call__(self):
		return self._left_expr() - self._right_expr()



class Number:
	'''Caso base para recursão.'''

	def accept(self, visitor):
		return visitor.visit_number(self)

	def __init__(self, num):
		self._num = num

	def __call__(self):
		return self._num


class Visitor:

	def visit_number(self, number):
		return str(number._num)

	def visit_add(self, sum_expression):
		return '(' + sum_expression._left_expr.accept(self) + ' + ' + sum_expression._right_expr.accept(self) + ')'

	def visit_substraction(self, substraction_expression):
		return '(' + substraction_expression._left_expr.accept(self) + ' - ' + substraction_expression._right_expr.accept(self) + ')'		


if __name__ == '__main__':
	
	visitor = Visitor()

	number_5 = Number(5)
	number_2 = Number(2)
	assert number_5.accept(visitor) == '5'
	assert number_2.accept(visitor) == '2'

	sum_expression = Add(number_5, number_2)
	assert sum_expression.accept(visitor) == '(5 + 2)'

	substraction_expression = Substraction(number_5, number_2)
	assert substraction_expression.accept(visitor) == '(5 - 2)'

	complex_expression = Add(sum_expression, substraction_expression)
	assert visitor.visit_add(complex_expression) == '((5 + 2) + (5 - 2))'