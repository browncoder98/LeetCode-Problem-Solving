class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        c = x
        b = 0

        while c:
            b = b * 10 + c % 10
            c = c / 10
        return b == x


q = Solution2()
print(q.isPalindrome(121))