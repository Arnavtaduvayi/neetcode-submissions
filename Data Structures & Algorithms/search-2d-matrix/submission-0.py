class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # maybe if we find the middle collumn and middle row? We can set 
        # the r1c1 to be left and then 
        # The secret is that you can treat this as a 1d array by
        #just doing matrix[i // cols][i % cols]
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows*cols - 1
        mid = right // 2

        while left <= right :
            if matrix[mid // cols][mid % cols] == target :
                return True
            elif matrix[mid // cols][mid % cols] > target :
                right = mid - 1
                mid = left + ((right - left) // 2)
            else: 
                left = mid + 1
                mid = left + ((right - left) // 2)
        
        return False