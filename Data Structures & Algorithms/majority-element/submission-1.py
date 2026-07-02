class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)/2
        frq={}
        for i in nums:
            if i in frq:
                frq[i]+=1
            else:
                frq[i]=1
        for key in frq:
            if frq[key] > n:
                return key

        