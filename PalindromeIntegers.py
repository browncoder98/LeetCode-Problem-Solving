#Leetcode Problem: Palindrome Integers (Easy)

"""
9. Palindrome Number
Easy

Given an integer x, return true if x is a 
palindrome
 and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
	def isPalindrome(self, x:int) -> bool:
		if x < 0:
			return False
		div = 1
		print(div)
		print(x)
		while x>=10*div:
			print(div)
			div = div * 10
			print(div)
		while x:
			print(x)
			if x // div != x % 10:
				print(div)
				print(x)
				return False
			x = (x%div) // 10
			print(x)
			div = div / 100
			print(div)
			print(x)
		return True


p = Solution()
print(p.isPalindrome(x=1001))