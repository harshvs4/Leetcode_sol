class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx=0
        for i in range(len(matrix)):
            if target<=matrix[i][-1]:
                idx=i
                break
        for j in matrix[idx]:
            if j==target:
                return True
        return False
