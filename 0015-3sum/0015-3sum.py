class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer=[]
       
        for i in range(0,len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                tnums=nums[i]+nums[k]+nums[j]
                if(tnums==0):
                    answer.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    while(j<k and (nums[j]==nums[j-1])):
                        j=j+1
                    while(j<k and (nums[k]==nums[k+1])):
                        k=k-1
                elif(tnums<0):
                    j=j+1
                   
                else:
                    k=k-1
        return answer