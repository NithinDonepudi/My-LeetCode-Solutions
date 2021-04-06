class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for i in range(len(accounts)):
            x=0
            for j in range(len(accounts[0])):
                x=x+accounts[i][j]
            wealth.append(x)
        return max(wealth)
        