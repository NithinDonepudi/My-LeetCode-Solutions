class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                out.append(True)
            else:
                out.append(False)
        return out
        