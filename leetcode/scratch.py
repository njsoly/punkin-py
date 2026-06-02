
def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'


for i in (7, 11, 0, 100, -1):
	print('even_or_odd(', i, ') = ', even_or_odd(i), sep='')

