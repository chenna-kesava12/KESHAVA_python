class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self._expand(s, i, i)      # odd-length
            len2 = self._expand(s, i, i + 1)  # even-length
            long_len = len1 if len1 > len2 else len2
            if long_len > (end - start):
                start = i - (long_len - 1) // 2
                end = i + long_len // 2
        return s[start:end + 1]

    def _expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
        