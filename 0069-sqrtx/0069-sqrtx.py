class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            # Use integer division for comparison to avoid potential overflow
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1

        # The loop terminates when left > right. The answer is right, 
        # which is the largest integer whose square is less than or equal to x.
        return right

