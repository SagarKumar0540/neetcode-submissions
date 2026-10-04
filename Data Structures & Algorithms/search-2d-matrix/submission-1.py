class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index,arr in enumerate(matrix):
            left = 0
            right = len(arr) -1

            while left <= right:
                mid = (left + right) // 2

                if target == arr[mid]:
                    return True
                
                elif target >= arr[mid]:
                    left = mid +1 
                else:
                    right = mid -1
        return False        