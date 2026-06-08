class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, d = 0, len(matrix) - 1
        while t <= d:
            mid = (t+d) // 2
            if target < matrix[mid][0]:
                d = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                row = mid
                l, r = 0, len(matrix[row])
                while l <= r:
                    mid = (l+r)//2
                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
        return False
            
            

