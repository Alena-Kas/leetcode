"""
27. Remove Element (Easy)
Given an integer array nums, remove all occurrences of val in nums in-place
Time: O(N), Space: O(1)
"""


class Solution(object):
    def removeElement(self, nums, val):
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1

        return index
