class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        capacity = 0

        while l < r:
            width = r - l
            area = min(height[l], height[r]) * width

            capacity = max(capacity, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return capacity