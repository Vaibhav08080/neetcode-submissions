class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set(nums)
        if len(newset)-len(nums) == 0:
            return False
        else:
            return True   