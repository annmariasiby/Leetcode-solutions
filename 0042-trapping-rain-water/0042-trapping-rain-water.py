class Solution:
    def trap(self, height: List[int]) -> int:
       heightSize=len(height)
       l=[0]*heightSize
       r=[0]*heightSize
       n=0
       m=0
       ans=[0]*heightSize
       water=0
       if (heightSize<3):
        return 0
       for i in range(heightSize):
        if(m<height[i]):
            m=height[i]
        l[i]=m
       for i in range(heightSize-1,-1,-1):
        if(n<height[i]):
            n=height[i]
        r[i]=n
       for i in range(heightSize):
           ans[i]=min(l[i],r[i])
       for i in range(heightSize):
           if(ans[i]>height[i]):
                water+=ans[i]-height[i]
           else:
                water+=height[i]-ans[i]
        
       return water