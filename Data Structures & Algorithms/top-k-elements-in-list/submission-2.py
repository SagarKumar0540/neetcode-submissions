from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for index, num in enumerate(nums):
            num_freq[num] +=1
        
        sorted_nums = sorted(num_freq.keys(), key=lambda x: num_freq[x], reverse=True)
        return sorted_nums[:k]
        

        


