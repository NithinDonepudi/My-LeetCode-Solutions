class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        if needle=="":
            return 0
        
        for i in range(len(haystack)):
            if haystack[i:i+n]==needle:
                return i
        return -1
