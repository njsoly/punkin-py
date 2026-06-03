from leetcode.tester import show_call


def highest_and_lowest(numbers):
	ls = list(map(int, numbers.split()))
	return ' '.join([str(max(ls)), str(min(ls))])


if __name__ == '__main__':
	show_call(highest_and_lowest, "1 2 3 4 5")
	show_call(highest_and_lowest, "1 2 -3 4 5")
	show_call(highest_and_lowest, "1 9 3 4 -5")
	show_call(highest_and_lowest, "8 3 -5 42 -1 0 0 -9 4 7 4 -4")
