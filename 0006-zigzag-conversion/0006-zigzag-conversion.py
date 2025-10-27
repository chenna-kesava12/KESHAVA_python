class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If there is only one row or numRows >= length of string, return the string as is
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list to hold each row's characters
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        # Iterate through each character in the string
        for c in s:
            rows[curr_row] += c
            # Reverse direction if we are at top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            # Move to next row depending on direction
            curr_row += 1 if going_down else -1

        # Join all rows together
        return ''.join(rows)
