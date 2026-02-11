"""
14. Longest Common Prefix (Easy)
Find the longest common prefix string amongst an array of strings.
Time: O(N∗M), Space: O(1)
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        prefix = strs[0]
        nextid = 1

        while nextid < len(strs) and len(prefix) > 0:
            if strs[nextid].startswith(prefix):
                nextid += 1
            else:
                prefix = prefix[:-1]
        return prefix
