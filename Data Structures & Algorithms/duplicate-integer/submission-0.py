class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = {}
        for index,num in enumerate(nums):
            if num in my_list:
                return True
            my_list[num]=index
        return False
        