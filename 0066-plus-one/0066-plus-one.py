class Solution(object):
    def plusOne(self, digits):
        sum=0
        digits1=[]
        for i in range(len(digits)):
            sum=sum*10+digits[i]
        sum1=sum+1
        while(sum1!=0):
            digits1.append(sum1%10)
            sum1=sum1//10
        return digits1[::-1]

        