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
	test_set = [11, -12, 50, -40, 2]
	print('count_pos_sum_negs(', test_set, ') = ', count_pos_sum_negs(test_set))
