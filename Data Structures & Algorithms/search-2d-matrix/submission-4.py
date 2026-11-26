class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w = len(matrix[0])
        l, r = 0, len(matrix)*w - 1
    
       
        while l <= r:
            mid = l + ((r-l)//2)
            row, col = mid // w, mid % w
            
            if matrix[row][col] < target:
                l = mid + 1
                print(l)
            elif matrix[row][col] > target:
                r = mid - 1
            else: return True

        return False