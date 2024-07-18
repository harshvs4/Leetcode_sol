class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # Initialize the dp matrix with the same dimensions as the input matrix
        dp = [[0 for j in range(n)] for i in range(n)]

        # Copy the last row of the matrix to the dp matrix
        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]

        # Fill the dp matrix from the second-to-last row to the top
        for i in range(n-2, -1, -1):
            for j in range(n):
                one = dp[i+1][j]  # Directly below
                two = dp[i+1][j+1] if j < n-1 else float('inf')  # Below-right
                three = dp[i+1][j-1] if j > 0 else float('inf')  # Below-left
                
                dp[i][j] = matrix[i][j] + min(one, two, three)

        # The result is the minimum value in the first row of the dp matrix
        result = min(dp[0])
        return result
        
