"""
13. Roman to Integer (Easy)
Given a roman numeral s, convert it to an integer.
Time: O(N), Space: O(1)
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        roman = {'I': 1, 'V': 5,
                 'X': 10, 'L': 50,
                 'C': 100, 'D': 500,
                 'M': 1000}

        for i in range(len(s)):
            num = roman[s[i]]
            if i+1 < len(s):
                num2 = roman[s[i+1]]
            else:
                num2 = 0

            if num >= num2:
                res += num
            else:
                res -= num
        return res
