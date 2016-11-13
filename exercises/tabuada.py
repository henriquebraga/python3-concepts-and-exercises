def menu():
	print('Por favor escolha uma opção: \n')
	print('0 - Sair')
	print('1 - Adicionar')
	print('2 - Substrair')
	print('3 - Multiplicar')
	print('4 - Dividir')

def is_not_valid(op):
	if op not in(tuple(str(n) for n in range(5))):
		print('Desculpe, opção inválida :(')

def calc_number(type_operation, n1, n2):
	r = 0
	message = 'Você escolheu {0} !'
	if type_operation == '1':
		print(message.format('Adição'))
		r = n1 + n2
	elif type_operation == '2':
		print(message.format('Subtração'))
		r = n1 - n2
	elif type_operation == '3':
		print(message.format('Multiplicação'))
		r = n1 * n2
	elif type_operation == '4':
		print(message.format('Divisão'))
		r = n1 / n2	
	return int(r)



op = '-1'

while op != '0':
	menu()
	op = input()
	if op == '0':
		print('Saindo do programa... Obrigado!')
		break
		
	if is_not_valid(op):
		continue

	n1 = int(input('Favor digitar o primeiro número: '))
	n2 = int(input('Favor digitar o segundo número: '))

	r = calc_number(op, n1, n2)

	mul = 0

	print('Tabuada do {0}', r)
	
	while mul < 11:
		print('{0} x {1} = {2}'.format(r, mul, r * mul))
		mul += 1






