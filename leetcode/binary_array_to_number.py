from leetcode.tester import show_call


# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python


def binary_array_to_number(numbers):
	n = 0
	for bit in numbers:
		n = n * 2 + int(bit)
	return n


def binary_array_to_number_alt1(arr):
	return int("".join(map(str, arr)), 2)


def binary_array_to_number_alt2(arr):
	return int(''.join(str(a) for a in arr), 2)


if __name__ == '__main__':
	test_cases = [
		[1, 0, 1, 0],
		[1, 1, 1, 1],
		[0, 1, 1, 0],
	]
	for tc in test_cases:
		show_call(binary_array_to_number, tc)
		print()
	for tc in test_cases:
		show_call(binary_array_to_number_alt1, tc)
		print()
	for tc in test_cases:
		show_call(binary_array_to_number_alt2, tc)
		print()
