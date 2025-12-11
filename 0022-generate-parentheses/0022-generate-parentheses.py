class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(path, open_count, close_count):
            # If the current path has length 2*n, it's complete
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            # If we can add an open parenthesis, do it
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count)
                path.pop()  # backtrack
            
            # If we can add a close parenthesis, do it
            if close_count < open_count:
                path.append(")")
                backtrack(path, open_count, close_count + 1)
                path.pop()  # backtrack
        
        backtrack([], 0, 0)
        return res
        