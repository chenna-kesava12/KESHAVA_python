class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Current container dimensions
            h = min(height[left], height[right])
            width = right - left
            max_water = max(max_water, h * width)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
        