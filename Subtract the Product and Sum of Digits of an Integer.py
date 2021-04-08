class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sumd=0
        while n>0:
            rem=n%10
            prod=prod*rem
            sumd=sumd+rem
            n=int(n/10)
        dif=prod-sumd
        return dif
