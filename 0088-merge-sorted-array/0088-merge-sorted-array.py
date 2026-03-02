class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for nums1, nums2, and the position to insert in nums1
        p1 = m - 1
        p2 = n - 1
        p_merge = m + n - 1

        # While there are elements to consider in nums2
        while p2 >= 0:
            # If p1 is within bounds and the element at p1 is greater than p2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # Place the larger element from nums1 at the merge position
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else:
                # Place the element from nums2 (either p1 is out of bounds or nums2[p2] is larger/equal)
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            # Move the merge pointer down
            p_merge -= 1
        
        # Note: If there are remaining elements in nums1 (p1 >= 0), they are already in the correct place.

