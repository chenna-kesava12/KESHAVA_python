class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # If partition1 is 0, set left part as -infinity, else set it as nums1[partition1 - 1]
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            # If partition1 is at the end, set right part as +infinity, else set it as nums1[partition1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            # If partition2 is 0, set left part as -infinity, else set it as nums2[partition2 - 1]
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            # If partition2 is at the end, set right part as +infinity, else set it as nums2[partition2]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd length
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # Even length
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            # If maxLeft1 > minRight2, move partition1 to the left
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            # If maxLeft2 > minRight1, move partition1 to the right
            else:
                left = partition1 + 1
        
        raise ValueError("Input arrays are not sorted")
