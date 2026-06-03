from leetcode.tester import show_call


def filter_list(l):
	# 'return a new list with the strings filtered out'
	return [o for o in l if isinstance(o, int)]


if __name__ == '__main__':
	show_call(filter_list, [1, "snth", 3, [], 'b', 'c'])
	show_call(filter_list, [])
	show_call(filter_list, [1, 2, "aasf", "1", "123", 123])
