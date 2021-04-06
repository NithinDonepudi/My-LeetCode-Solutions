class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=0
        if len(strs)==0:
            return ""
        while n<len(min(strs)):
            pre=strs[0][n]
            for i in range(len(strs)):
                if strs[i][n]!=pre:
                    return strs[0][:n]
            n=n+1
        return strs[0][:n]