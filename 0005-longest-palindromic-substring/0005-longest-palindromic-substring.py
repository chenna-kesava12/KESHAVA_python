def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        # For odd length palindromes
        len1 = expand(s, i, i)
        # For even length palindromes
        len2 = expand(s, i, i + 1)
        
        long_len = max(len1, len2)
        
        if long_len > (end - start):
            start = i - (long_len - 1) // 2
            end = i + long_len // 2
    
    return s[start:end + 1]


def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
        