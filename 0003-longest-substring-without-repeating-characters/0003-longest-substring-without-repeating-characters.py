class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # stores last index of each character
        left = 0  # left boundary of the window
        max_len = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
