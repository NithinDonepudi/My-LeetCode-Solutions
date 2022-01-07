class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x=0
        h=[]
        sr=''
        if numRows==1:
            return s
        for i in range(len(s)):
            x=min(i%((2*numRows)-2),((2*numRows)-2)-i%((2*numRows)-2))
            h.append(x)
        for j in range(numRows):
            for i in range(len(s)):
                if h[i]==j:
                    sr=sr+s[i]
        return sr
