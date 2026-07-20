class Solution:
    def intersection(self, nums1, nums2):

        s1 = set(nums1)

        ans = set()

        for x in nums2:
            if x in s1:
                ans.add(x)

        return list(ans)

              
       