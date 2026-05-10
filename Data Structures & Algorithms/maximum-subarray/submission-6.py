class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub,Cursum=nums[0],0
        for num in nums:
            if Cursum<0:
                Cursum=0
            Cursum+=num
            maxSub=max(Cursum, maxSub)
        return maxSub
        