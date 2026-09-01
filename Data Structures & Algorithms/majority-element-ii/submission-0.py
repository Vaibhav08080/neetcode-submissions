from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        n=len(nums)
        res=[]
        for i in c:
            if c[i]>n//3:
                res.append(i)
        return res        