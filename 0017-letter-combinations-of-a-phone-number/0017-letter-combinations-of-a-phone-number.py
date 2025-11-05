class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            # If full combination formed, add to result
            if index == len(digits):
                res.append("".join(path))
                return

            # Get letters for current digit
            for ch in phone_map[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()  # backtrack (remove last letter)

        backtrack(0, [])
        return res
