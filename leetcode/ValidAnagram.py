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
	def isAnagram(self, s: str, t: str) -> bool:
		if np.strings.str_len(s) != np.strings.str_len(t):
			return False
		
		for i in range(len(s)):
			t = t.replace(s[i], '', 1)
		
		if t == '':
			return True
		return False
	
	def isAnagram2(self, s: str, t: str) -> bool:
		if np.strings.str_len(s) != np.strings.str_len(t):
			return False
		
		for i in range(len(s)):
			t = t.replace(s[i], '', 1)
		
		if t == '':
			return True
		return False


if __name__ == '__main__':
	test_cases = [
		(("anagram", "nagaram"), True),
		(("rat", "car"), False),
		(("", ""), True),
		(("a", "a"), True),
		(("ab", "a"), False),
	]
	
	solution = Solution()
	solution_approaches = [solution.isAnagram]
	for approach in solution_approaches:
		print(f'Approach: {approach.__name__}')
		for (s, t), expected in test_cases:
			result = show_call(approach, s, t)
			status = 'OK' if result == expected else f'FAIL (expected {expected!r})'
			print(f'  -> {status}\n')
