class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for j in words:
            tot=0
            for i in range(len(allowed)):
                tot=tot+j.count(allowed[i])
            if tot==len(j):
                count=count+1
        return count