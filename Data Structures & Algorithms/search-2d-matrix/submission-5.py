class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            rows, cols = len(matrix), len(matrix[0])

            i = 0
            j = cols-1

            while i < len(matrix) and j >= 0:
                m = matrix[i][j]

                if target == m:
                    return True
                elif target > m:
                    i += 1
                else:
                    j -= 1
            
            return False