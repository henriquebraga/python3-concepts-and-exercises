#-*- coding: utf -*-

from datetime import date
from abc import ABCMeta, abstractmethod


class Order:

	def __init__(self, customer, value):
		self.__customer = customer
		self.__value = value
		self.__status = 'NEW'
		self.__end_date = None

	def pay(self):
		self.__status = 'PAID'

	def end(self):
		self.__status = 'DELIVERED'
		self.__end_date = date.today()

	@property
	def customer(self):
		return self.__customer

	@property
	def value(self):
		return self.__value

	@property
	def status(self):
		return self.__status

	@property
	def end_date(self):
		return self.__end_date


class WorkQueue:

	def __init__(self):
		self.__commands = []

	def add(self, command):
		self.__commands.append(command)

	@property	
	def total_commands(self):
		return len(self.__commands)


	def process(self):
		for command in self.__commands:
			command.execute()


class Command:

	__metaclass__ = ABCMeta

	@abstractmethod
	def execute(self):
		pass


class FinishOrder(Command):

	def __init__(self, order):
		self.__order = order

	def execute(self):
		self.__order.end()


class PayOrder(Command):

	def __init__(self, order):
		self.__order = order

	def execute(self):
		self.__order.pay()


if __name__ == '__main__':

	order = Order(customer='Henrique Braga', value=50)
	
	assert order.customer == 'Henrique Braga'
	assert order.value == 50
	assert order.status == 'NEW'
	assert not order.end_date

	order.pay()

	assert order.status == 'PAID'

	order.end()

	assert order.status == 'DELIVERED'
	assert order.end_date == date.today()

	order = Order(customer='Henrique Braga', value=200)
	order_2 = Order(customer='Test', value=800)
	
	work_queue = WorkQueue()
	
	work_queue.add(PayOrder(order))
	assert work_queue.total_commands == 1
	
	work_queue.add(FinishOrder(order))
	assert work_queue.total_commands == 2

	work_queue.add(PayOrder(order_2))
	assert work_queue.total_commands == 3

	work_queue.process()
	assert order.status == 'DELIVERED'
	assert order_2.status == 'PAID'