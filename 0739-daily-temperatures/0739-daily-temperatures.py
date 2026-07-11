class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        answer=[0]*n
        s=[]
        for i in range(n):
            while(s and (temperatures[i]>temperatures[s[-1]])):
                 a=s.pop()
                 answer[a]=i-a
            s.append(i)
        return answer