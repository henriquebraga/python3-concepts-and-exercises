# -*- coding: utf-8 -*- 

def imprime(nota_fiscal):
	
	print('Imprimindo nota fiscal {cnpj}'
		.format(
			cnpj=nota_fiscal._cnpj)
			)

def salva_no_banco(nota_fiscal):
	
	print('Salvando nota fiscal {cnpj} no BD'
		.format(
				cnpj=nota_fiscal._cnpj)
			)
