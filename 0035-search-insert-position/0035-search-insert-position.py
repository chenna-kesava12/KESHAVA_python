class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Iterate through the list of numbers with their indices
        for i in range(len(nums)):
            # If the current number is greater than or equal to the target, 
            # it means the target should be inserted at or before this index.
            if nums[i] >= target:
                return i
        
        # If the loop finishes without returning (i.e., the target is larger than all elements), 
        # it should be inserted at the very end of the list.
        return len(nums)

# Example Usage:
# sol = Solution()
# print(sol.searchInsert([1,3,5,6], 5)) # Output: 2
# print(sol.searchInsert([1,3,5,6], 2)) # Output: 1
# print(sol.searchInsert([1,3,5,6], 7)) # Output: 4
# print(sol.searchInsert([1,3,5,6], 0)) # Output: 0
