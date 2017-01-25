class Criador_de_Nota_Fiscal:

	def __init__(self):

		self._razao_social = None
		self._cnpj = None
		self._data_de_emissao = None
		self._itens = None
		self._detalhe = None

	def com_razao_social(self, razao_social):
		self.__razao_social = razao_social
		return self

	def com_cnpj(self, cnpj):
		self._cnpj = cnpj
		return self

	def com_itens(self, itens):
		self._itens = itens
		return self

	def com_detalhes(self, detalhe):
		self._detalhe = detalhe 	
		return self

	def constroi(self):

		if self._razao_social is None:
			raise Exception('Razão social deve ser preenchida.')
		if self._cnpj is None:
			raise Exception('CNPJ deve ser preenchido.')
		if self._itens is None:
			raise Exception('Itens deve ser preenchidos.')
		if self._data_de_emissao is None:
			raise Exception('Data de emissão deve ser preenchida.')

		return NotaFiscal(razao_social=self._razao_social,
						  cnpj=self._cnpj,
						  data_de_emissao=self._data_de_emissao)