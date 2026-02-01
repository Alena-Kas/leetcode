"""
28. Find the Index of the First Occurrence in a String (Easy)
Given two strings, return the index of the first occurrence
Time: O(N∗M), Space: O(1)
"""


class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
