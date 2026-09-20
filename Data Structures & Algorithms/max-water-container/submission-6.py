class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxarea=0
        while i<=j:
            h=min(heights[j] , heights[i])
            w=j-i
            area=h*w
            maxarea=max(area , maxarea)
            if heights[j]>heights[i]:
                i+=1
            else:
                j-=1
        return maxarea