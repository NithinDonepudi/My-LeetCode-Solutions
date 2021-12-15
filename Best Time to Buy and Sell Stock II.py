class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Have=False
        Profit=Buy=Sell=0
        for i in range(len(prices)):
            if i<(len(prices)-1):
                if prices[i]<prices[i+1] and Have==False:
                    Have=True
                    Buy=prices[i]
                    print("buy")
                elif prices[i]>prices[i+1] and Have==True:
                    Have=False
                    Sell=prices[i]
                    Profit=Profit+Sell-Buy
                    print("sell")
            if i==len(prices)-1 and Have==True and prices[i]>Buy:
                Have=False
                Sell=prices[i]
                Profit=Profit+Sell-Buy
                print("buy last")
        return Profit
        
