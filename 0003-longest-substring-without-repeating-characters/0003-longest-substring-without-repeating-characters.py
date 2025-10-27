class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}  # Dictionary to store the most recent index of each character
        start = 0  # Start index of the current window
        max_len = 0  # Maximum length of substring without repeating characters

        for end, char in enumerate(s):  # `end` is the right pointer of the window
            if char in char_index_map and char_index_map[char] >= start:
                # If the character is already in the window, move the `start` pointer
                # to the right of the last occurrence of this character
                start = char_index_map[char] + 1

            # Update the most recent index of the current character
            char_index_map[char] = end

            # Update the maximum length of the substring
            max_len = max(max_len, end - start + 1)

        return max_len

        