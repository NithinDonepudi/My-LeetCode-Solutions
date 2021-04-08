class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        for i in range(len(items)):
            if ruleKey=='type' and ruleValue==items[i][0]:
                count=count+1
            elif ruleKey=='color' and ruleValue==items[i][1]:
                count=count+1
            elif ruleKey=='name' and ruleValue==items[i][2]:
                count=count+1
        return count
