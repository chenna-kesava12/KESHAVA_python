class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  # Initialize with first triplet
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If exact match, return immediately
                if current_sum == target:
                    return target
                
                # Update closest_sum if this sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
