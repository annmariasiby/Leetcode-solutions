class Solution(object):
    def runningSum(self, nums):

        nums1=[0]*len(nums)
        nums1[0]=nums[0]
        for i in range(1,len(nums)):
            nums1[i]=nums1[i-1]+nums[i]
        return nums1
        