def count_pos_sum_negs(my_list):
	if not my_list: return []
	
	pos, sum_of_negs = 0, 0
	for n in my_list:
		if n > 0:
			pos += 1
		else:
			sum_of_negs += n
	
	return [pos, sum_of_negs]


if __name__ == '__main__':
	from tester import show_call
	show_call(count_pos_sum_negs, [11, -12, 50, -40, 2])
	show_call(count_pos_sum_negs, [])
	show_call(count_pos_sum_negs, [-1, -2, -3])
