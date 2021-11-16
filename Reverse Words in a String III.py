class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(" ")
        x=''
        for word in words:
            word=word[::-1]
            x=x+word+' '
        return x[:-1]
