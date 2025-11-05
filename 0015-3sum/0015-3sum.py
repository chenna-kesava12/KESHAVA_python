class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right in-place
                    left_val, right_val = nums[left], nums[right]
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1

        return res
