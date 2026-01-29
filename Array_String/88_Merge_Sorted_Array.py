"""
88. Merge Sorted Array (Easy)
Merge two sorted arrays nums1 (size m+n) and nums2 (size n)into nums1 in-place.
Time: O(M+N), Space: O(1)
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        indx1 = m-1
        indx2 = n-1
        indx = m + n - 1

        while indx2 >= 0:
            if indx1 >= 0 and nums1[indx1] > nums2[indx2]:
                nums1[indx] = nums1[indx1]
                indx1 -= 1
            else:
                nums1[indx] = nums2[indx2]
                indx2 -= 1
            indx -= 1
        return nums1
