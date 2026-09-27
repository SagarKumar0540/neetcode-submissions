class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_result = {}
        for index,num in enumerate(nums):
            complement = target-num
            if complement in prev_result:
                return [prev_result[complement],index]
            prev_result[num]=index
        return []
        
