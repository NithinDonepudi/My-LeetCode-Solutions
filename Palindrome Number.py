class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        if (x<0):
            return False
        else:
            rev=0
            rem=0
            while x>0:
                rem=x%10
                rev=rev*10+rem
                x=int(x/10)
            if temp==rev:
                return True
            else:
                return False