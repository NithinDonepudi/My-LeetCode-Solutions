class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        high=(2**31)-1
        low=-2**31
        num=0
        pos=1
        if s=='':
            return num
        if ord(s[0]) in range(48,58) or ord(s[0]) in [43,45]:
            i=0
            if ord(s[0]) in [43,45]:
                i=1
                if ord(s[0])==45:
                    pos=-1
            while(i<len(s) and ord(s[i]) in range(48,58)):
                num=num*10+int(s[i])
                i=i+1
        else:
            return num
        num=num*pos
        if num>high:
            return high
        if num<low:
            return low
        return num
        
