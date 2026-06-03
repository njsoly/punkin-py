
def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'


for i in (7, 11, 0, 100, -1):
	print('even_or_odd(', i, ') = ', even_or_odd(i), sep='')


def remove_every_other(my_list):
	return my_list[0::2]


test_set = [11, 12, 50, 40, 2]
print('remove_every_other(', test_set, ') = ', remove_every_other(test_set))
