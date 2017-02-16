#-*- coding: utf-8 -*-

from datetime import date
from copy import copy


class Contract:

	def __init__(self, date, customer, _type):
		self.__date = date
		self.__customer = customer
		self.__type = _type

	@property
	def date(self): 
		return self.__date

	@date.setter
	def date(self, date):
		self.__date = date

	@property
	def customer(self):
		return self.__customer

	@customer.setter
	def customer(self, customer):
		self.__customer = customer

	@property
	def _type(self):
		return self.__type

	def advance(self):
		if self.__type == 'NEW':
			self.__type = 'IN_PROGRESS'

		elif self.__type == 'IN_PROGRESS':
			self.__type = 'ACCEPTED'

		elif self.__type == 'ACCEPTED':
			self.__type = 'OK'

	def save_state(self):
		clone = copy(self)
		return clone

	def restore(self, state):
		self.customer = state.customer
		self.date = state.date
		self.__type = state._type




class History:
	'''Lista de estados salvo. (Poderia guardar a lista de contratos salvos diretamente aqui), porém
	 encapsulando o contrato dentro da classe estado, deixa mais claro que o que está guardando é um 
	 estado de um contrato -> código mais expressivo. '''

	def __init__(self):
		self.__last_states = []

	def get_state(self, index):
		try:
			return self.__last_states[index]
		
		except IndexError:
			return None

	def add_state(self, state):
		self.__last_states.append(state)

	def __getitem__(self, pos):
		try:
			return self.__last_states[pos]
		except IndexError:
			return None

	def __len__(self):
		return len(self.__last_states)


if __name__ == '__main__':
	
	from datetime import date

	history = History()
	contract = Contract(date=date.today(),
						customer='Henrique Braga',
						_type='NEW')

	assert not history[0]
	assert contract.customer == 'Henrique Braga'
	assert contract.date == date.today()
	assert contract._type == 'NEW'

	#Advancing the contract (should be IN_PROGRESS)
	contract.advance()
	assert contract._type == 'IN_PROGRESS'

	#Contract should not be the same ref as copy_contract
	copy_contract = contract.save_state()

	assert copy_contract is not contract

	#Contract should have the same customer, date, type from ccontract.
	assert copy_contract.customer == contract.customer
	assert copy_contract.date == contract.date
	assert copy_contract._type == contract._type


	#Adding the current state from contract
	contract.customer = 'Anything'
	history.add_state(contract.save_state())

	#History should have one state at position 0.
	assert history[0]._type == 'IN_PROGRESS'

	contract.advance()
	assert contract._type == 'ACCEPTED'
	

	history.add_state(contract.save_state())
	
	assert len(history) == 2
	assert history[0]._type == 'IN_PROGRESS'
	assert history[1]._type == 'ACCEPTED'

	#State should restore to previous state from History (status ACCEPTED)
	contract.restore(history[1])
	assert contract._type == history[1]._type
	assert contract.customer == history[1].customer
	#State should restore to the first state in History(status IN_PROGRESS)
	contract.restore(history[0])
	assert contract._type == history[0]._type












		