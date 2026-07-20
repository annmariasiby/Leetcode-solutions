class Solution(object):
    def majorityElement(self, nums):
       freq={}
       for n in nums:
           freq[n]=freq.get(n,0)+1
       for k,v in freq.items():
           if v>len(nums)//2:
            return k