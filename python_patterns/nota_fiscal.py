# -*- coding: utf-8 -*-
from datetime import date
import observers 


class Item:

	def __init__(self, descricao, valor):
		self._descricao = descricao
		self._valor = valor

	@property
	def descricao(self):
		return self._descricao

	@property
	def valor(self):
		return self._valor


class NotaFiscal:

	def __init__(self, razao_social, cnpj, itens,
				 data_emissao=date.today(), detalhes='',
				 observers=[observers.imprime, observers.salva_no_banco]):
		self._razao_social = razao_social
		self._cnpj = cnpj
		self._data_emissao = data_emissao

		if len(detalhes) > 20:
			raise Exception('Detalhes da nota não pode ter mais que 20 caracteres.')

		self._detalhes = detalhes
		self._itens = itens

		[observer_action(self) for observer_action in observers]


if __name__ == '__main__':

	NotaFiscal(
				razao_social='Henrique',
				cnpj='123456789',
				itens=[
						Item('Item Legal', 2), 
						Item('Item Legal 2', 3)
					]
			   )

