class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # If this sum is closer to the target, update closest_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                # Move pointers based on comparison
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # Exact match — can't get closer
                    return curr_sum

        return closest_sum
