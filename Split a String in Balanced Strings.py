class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        tcount=0
        for i in range(len(s)):
            if s[i]=='L':
                count=count+1
            elif s[i]=='R':
                count=count-1
            if count==0:
                tcount=tcount+1
        return tcount
                