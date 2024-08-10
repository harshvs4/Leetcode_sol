class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or the string length is less than numRows
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize an array to store each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Traverse the string
        for char in s:
            rows[current_row] += char
            # Change direction if we are at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row
            current_row += 1 if going_down else -1

        # Concatenate all rows to get the final string
        return ''.join(rows)

