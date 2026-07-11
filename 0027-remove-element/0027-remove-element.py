class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.__delitem__(i)
                nums.append(0)
                leng -= 1

        return leng