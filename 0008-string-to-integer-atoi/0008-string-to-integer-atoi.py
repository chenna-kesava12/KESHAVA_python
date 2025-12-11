class Solution:
    def myAtoi(self, s):
        INT_MIN = -2**31          # -2147483648
        INT_MAX = 2**31 - 1       #  2147483647
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # If string ended
        if i >= n:
            return 0
        
        # 2. Check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 3. Convert digits
        result = 0
        found_digit = False
        
        while i < n and s[i].isdigit():
            found_digit = True
            digit = ord(s[i]) - ord('0')
            i += 1
            
            # Check overflow BEFORE adding digit
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
        
        if not found_digit:
            return 0
        
        return sign * result


        