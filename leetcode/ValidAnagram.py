import random

import numpy as np

from tester import show_call


'''
242. Valid Anagram
Solved
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''


class Solution:
	@staticmethod
	def isAnagram(s: str, t: str) -> bool:
		if np.strings.str_len(s) != np.strings.str_len(t):
			return False
		
		for i in range(len(s)):
			t = t.replace(s[i], '', 1)
		
		if t == '':
			return True
		return False
	
	@staticmethod
	def isAnagram2(s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		
		lt = list(t)
		for ch in s:
			try:
				lt.remove(ch)
			except ValueError:
				return False
		
		return len(lt) == 0
	
	## Claude's. ##
	# Although, it looks a lot like my first idea, but with numpy's C-level sorting.
	@staticmethod
	def isAnagram3_byClaude(s: str, t: str) -> bool:
		if np.strings.str_len(s) != np.strings.str_len(t):
			return False
		
		return np.array_equal(np.sort(np.frombuffer(s.encode(), dtype = np.uint8)),
		                      np.sort(np.frombuffer(t.encode(), dtype = np.uint8)))
	
	@staticmethod
	def isAnagram4(s: str, t: str) -> bool:
		if np.not_equal(np.strings.str_len(s), np.strings.str_len(t)):
			return False
		
		t_arr = np.array(t)
		
		for ch in s:
			t_arr = np.strings.replace(t_arr, ch, '', 1)
		
		return bool(np.strings.equal(t_arr, ''))
	
	@staticmethod
	def isAnagram5(s: str, t: str) -> bool:
		if np.strings.str_len(s) != np.strings.str_len(t):
			return False
		elif np.strings.str_len(s) <= 2:
			return s == t or s == t[::-1]
		
		for i in range(len(s)):
			t = t.replace(s[i], '', 1)
		
		return t == ''

if __name__ == '__main__':
	random.seed(42)
	_s_big = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k = 1000))
	_t_big = ''.join(random.sample(_s_big, len(_s_big)))
	
	# print(_s_big)
	# print(_t_big)

	test_cases = [
		(("anagram", "nagaram"), True),
		(("rat", "car"), False),
		(("", ""), True),
		(("a", "a"), True),
		(("ab", "a"), False),
		(("aoeusqnjtkhaxoeusnthqjkx", "qjkxqjkxaoeusnthaoeusnth"), True),
		(("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
		  "xwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"), True),
		(("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
		  "xxvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"), False),
		((_s_big, _t_big), True),
	]

	solution = Solution()
	solution_approaches = [
		solution.isAnagram,
		solution.isAnagram2,
		solution.isAnagram3_byClaude,
		solution.isAnagram4,
		solution.isAnagram5,
	]


	for approach in solution_approaches:
		print(f'Approach: {approach.__name__}')
		for (s, t), expected in test_cases:
			result = show_call(approach, s, t)
			status = 'OK' if result == expected else f'FAIL (expected {expected!r})'
			print(f'  -> {status}')
