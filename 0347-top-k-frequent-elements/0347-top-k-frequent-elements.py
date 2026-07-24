class Solution(object):
    def topKFrequent(self, nums, k):
       freq={}
       for n in nums:
           freq[n]=freq.get(n,0)+1
       sortedarr=sorted(freq,key=freq.get,reverse=True)
       return sortedarr[:k]
        