class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_0=nums.count(0)
        nums1=nums.count(1)
        nums2=nums.count(2)
        nums[:]=[0]*num_0+[1]*nums1+nums2*[2]
        