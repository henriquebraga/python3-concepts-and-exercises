#-*- coding: UTF-8 -*-

class Budget:

	def __init__(self):
		self._items = []


	@property
	def value(self):
		return sum(item.value for item in self._items)
		
	def get_items(self):
		return tuple(self._items)

	def total_items(self):
		return len(self._items)

	def add_item(self, item):
		self._items.append(item)

	
class Item:

	def __init__(self, name, value):
		self._name = name
		self._value = value

	@property
	def name(self):
		return self._name

	@property
	def value(self):
		return self._value



class FiveItemsDiscount:

	def __init__(self, next):
		self._next = next

	def calculate(self, budget):
		if budget.total_items > 5:
			return budget.value * 0.1
		else:
			return self._next.calculate(budget)

class MoreThan500Discount:
	def __init__(self, next):
		self._next = next

	def calculate(self, budget):
		if budget.value > 500:
			return budget.value * 0.07
		else:
			return self._next.calculate(budget)

class NoDiscount:

	def calculate(self, budget):
		return 0



class TaxCalculator:

	def calculate_taxes(self, budget):
		discount = FiveItemsDiscount(
				 		MoreThan500Discount(
				 			NoDiscount()
				 		)
				)

		return discount.calculate(budget)

if __name__ == '__main__':
	budget = Budget()
	budget.add_item(Item('Item A', 100.0))
	budget.add_item(Item('Item B', 50.0))
	budget.add_item(Item('Item C', 400.0))
	budget.add_item(Item('Item C', 400.0))
	budget.add_item(Item('Item C', 400.0))
	budget.add_item(Item('Item C', 400.0))

	discount = TaxCalculator().calculate_taxes(budget)
	print(discount)




