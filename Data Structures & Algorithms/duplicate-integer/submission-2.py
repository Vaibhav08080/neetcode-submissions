class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))-len(nums)==0:
            return False
        else:
            return True    
        