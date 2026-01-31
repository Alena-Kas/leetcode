"""
58. Length of Last Word (Easy)
Given a string s consisting of words and spaces,
return the length of the last word in the string.
Time: O(N), Space: O(N)
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        res = s.strip().split()
        return len(res[-1])
