class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        for c in s:
            rows[curr_row] += c
            # Change direction at the first or last row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        # Concatenate all rows
        return ''.join(rows)
