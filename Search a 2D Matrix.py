class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        r=len(matrix)
        c=len(matrix[0])
        xi=-1
        for i in range(r):
            if target==matrix[i][c-1]:
                return True
            if target<matrix[i][c-1]:
                xi=i
                break
        if xi == -1:
            return False
        
        for j in range(c-2,-1,-1):
            if target == matrix[xi][j]:
                return True
            
        return False
        
        