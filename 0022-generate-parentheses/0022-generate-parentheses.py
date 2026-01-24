class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(open_count, close_count, path):
            # If the current string has length 2*n, it's complete
            if len(path) == 2 * n:
                result.append(path)
                return

            # If we can add another '(', do it
            if open_count < n:
                backtrack(open_count + 1, close_count, path + "(")

            # If we can add ')', do it
            if close_count < open_count:
                backtrack(open_count, close_count + 1, path + ")")

        backtrack(0, 0, "")
        return result
