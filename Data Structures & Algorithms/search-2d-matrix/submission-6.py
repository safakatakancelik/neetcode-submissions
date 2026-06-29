class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # row count
        n = len(matrix[0]) # column count
        list_to_check = []
        
        for i in range(m):
            try:
                if matrix[i][0] <= target < matrix[i + 1][0]:
                    list_to_check = matrix[i]
                    break
            except:
                list_to_check = matrix[-1]

        if list_to_check.count(target) > 0:
            return True
        else:
            return False
        
