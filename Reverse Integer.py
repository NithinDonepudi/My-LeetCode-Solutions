class Solution:
    def reverse(self, x: int) -> int:
        low=-2**31
        high=2**31-1
        neg=0
        temp=x
        if (x<0):
            neg=1
            x=x*-1
        rev=0
        rem=0
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=int(x/10)
        if rev>high or temp<low:
            return 0
        elif (neg==0):
            return rev
        else:
            return rev*-1
        