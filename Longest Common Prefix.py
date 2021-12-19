class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min=201
        if len(strs)==1:
            return strs[0]
        for i in strs:
            if len(i)<min:
                min=len(i)
        count=0
        while count!=len(strs)-1:
            count=0
            for j in range(len(strs)-1):
                if strs[j][:min]==strs[j+1][:min]:
                    #print(strs[j][:min])
                    count=count+1
            if count==len(strs)-1:
                return strs[j][:min]
            else:
                min=min-1
        return ""
