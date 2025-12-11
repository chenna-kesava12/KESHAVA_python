class Solution:
    def isValid(self, s):
        stack = []
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():
                # If opening bracket, push to stack
                stack.append(char)
            elif char in bracket_map:
                # If closing bracket, check if top matches
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (not required here but safe)
                return False
        
        # Valid if stack is empty
        return not stack

        