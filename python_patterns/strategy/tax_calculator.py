#-*- coding: UTF-8 -*-

class Budget:

	def __init__(self, value):
		self._value = value

	@property
	def value(self):
		return self._value


def ICMS(budget):
	return budget.value * 0.05

def ISS(budget):
	return budget.value * 0.08

def calculate_tax(budget, tax):
	return tax(budget)

if __name__ == '__main__':
	budget = Budget(10)
	print(calculate_tax(budget, ICMS))
	print(calculate_tax(budget, ISS))

	