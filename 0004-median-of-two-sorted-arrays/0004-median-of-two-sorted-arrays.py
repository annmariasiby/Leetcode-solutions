class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=nums1+nums2
        num3.sort()
        n=len(nums1)
        m=len(nums2)
        if (m+n)%2==0:
            new=(m+n)//2
            new1=((m+n)//2) +1
            return (num3[new-1]+num3[new1-1])/2
           
        else:
            new2=((m+n)//2)+1
            return num3[new2-1]

