class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        nmax=0
        for i in range(len(s)):
            if s[i]=='(':
                count=count+1
            elif s[i]==')':
                count=count-1
            if nmax<count:
                nmax=count
        return nmax
            