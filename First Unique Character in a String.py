class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos=-1
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return pos
