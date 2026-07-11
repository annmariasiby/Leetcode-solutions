class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        e=0
        for i in range(len(nums)):
            e=e^nums[i]
        return e