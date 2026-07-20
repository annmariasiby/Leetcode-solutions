class Solution(object):
    def pivotIndex(self, nums):
        lsum=0
        rsum=0
        total=sum(nums)
        for i in range(len(nums)):
            rsum=total-lsum-nums[i]
            if lsum==rsum:
                return i
            else:
                lsum=lsum+nums[i]
        return -1

        