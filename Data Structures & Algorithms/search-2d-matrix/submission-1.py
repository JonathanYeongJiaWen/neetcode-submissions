class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        length = len(matrix[0])
        t, d, l, r = 0, height-1, 0, length-1
        while t<=d:
            mid = (t+d)//2
            if target < matrix[mid][l]:
                d = mid - 1
            elif target > matrix[mid][r]:
                t = mid + 1
            else:
                row = mid
                break
        if t>d:
            return False
        while l<=r:
            mid = (l+r)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
