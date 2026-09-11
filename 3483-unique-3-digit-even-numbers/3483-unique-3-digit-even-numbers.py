class Solution(object):
    def totalNumbers(self, digits):
        ans=[]
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or k==i:
                        continue
                    if digits[i]==0:
                        continue
                    if digits[k]%2!=0:
                        continue
                    num=100*digits[i]+10*digits[j]+digits[k]
                    if num not in ans:
                        ans.append(num)
        return len(ans)

        