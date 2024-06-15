class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Identify rows and columns that need to be zeroed.
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use the first row and first column to mark zero rows and columns.
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Zero out cells based on marks in the first row and first column.
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Step 3: Zero out the first row if necessary.
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: Zero out the first column if necessary.
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

