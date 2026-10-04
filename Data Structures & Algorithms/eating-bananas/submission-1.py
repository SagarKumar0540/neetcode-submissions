import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            total_hours = 0

            for p in piles:
                total_hours += math.ceil(p / mid)
            
            if total_hours <= h:
                ans = mid
                high = mid -1
            else:
                low = mid +1
        return ans