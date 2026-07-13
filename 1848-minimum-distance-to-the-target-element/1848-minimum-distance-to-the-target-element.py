class Solution(object):
    def getMinDistance(self, nums, target, start):
        minimum=900000
        for i in range(len(nums)):
            if nums[i]==target:
                k=i
                minimum=min(minimum,abs(k-start))
                
        return minimum
        