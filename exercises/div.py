44
def calc_div():
	n = int(input('Digite o dividendo: '))
	div = int(input('Digite o divisor: '))
	r = 0
	while div <= n:
		n-= div
		r+= 1

	print(r, n)


if __name__ == '__main__':
	calc_div()

