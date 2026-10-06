class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        
        m,n = len(nums1), len(nums2)
        total_len = m+n
        half_len = (total_len +1) // 2

        low = 0
        high = m

        while low <= high:
            i = low+ ( high - low) // 2
            j = half_len - i 

            a_left = nums1[i-1] if i > 0 else float('-inf')
            a_right = nums1[i] if i < m else float('inf')
            b_left = nums2[j-1] if j > 0 else float('-inf')
            b_right = nums2[j] if j < n else float('inf')

            if a_left <= b_right and b_left <= a_right:
                
                if total_len % 2 != 0:
                    return float(max(a_left,b_left))

                return (max(a_left,b_left) + min(a_right,b_right)) / 2.0
            elif a_left > b_right:
                high = i -1
            else :
                low = i +1
        return 0.0