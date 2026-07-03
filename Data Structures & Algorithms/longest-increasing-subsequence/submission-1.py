class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(len(nums))]
        
        def solve(i,p):
            if i ==n:
                return 0
            take=0    
            if p==-1 or nums[p]<nums[i]:
                take=1+solve(i+1,i)
            if dp[i][p+1]!=-1:
                return dp[i][p+1]
            skip=solve(i+1,p)     
            dp[i][p+1]=max(skip , take )
            return dp[i][p+1]
        return solve(0,-1)