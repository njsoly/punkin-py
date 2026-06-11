from leetcode.tester import show_call


"""
This is a very basic python problem, to get back into the swing.
It's not actually from LeetCode, it's from CodeWars.

https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""



def highest_and_lowest(numbers):
	ls = list(map(int, numbers.split()))
	return ' '.join([str(max(ls)), str(min(ls))])


def highest_and_lowest2(numbers):
	nums = sorted([int(n) for n in numbers.split()])
	return f'{nums[-1]} {nums[0]}'

if __name__ == '__main__':
	test_cases = [
		"1 2 3 4 5",
		"1 2 -3 4 5",
		"1 9 3 4 -5",
		"8 3 -5 42 -1 0 0 -9 4 7 4 -4",
	]
	for tc in test_cases:
		show_call(highest_and_lowest, tc)
	print()
	for tc in test_cases:
		show_call(highest_and_lowest2, tc)
