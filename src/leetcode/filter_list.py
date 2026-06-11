from leetcode.tester import show_call


"""
This is a very basic python problem, to get back into the swing.
It's not actually from LeetCode, it's from CodeWars.
"""


# 'return a new list with the strings filtered out'
def filter_list(l):
	# the following statement utilizes a list comprehension
	return [o for o in l if isinstance(o, int)]


if __name__ == '__main__':
	show_call(filter_list, [1, "snth", 3, [], 'b', 'c'])
	show_call(filter_list, [])
	show_call(filter_list, [1, 2, "aasf", "1", "123", 123])
