def count_pos_sum_negs(my_list):
	pos = sum(1 for n in my_list if n > 0)
	sum_of_negs = 0
	for n in my_list:
		if n < 0:
			sum_of_negs = sum_of_negs + n
	
	return [pos, sum_of_negs]


test_set = [11, -12, 50, -40, 2]
print('count_pos_sum_negs(', test_set, ') = ', count_pos_sum_negs(test_set))
