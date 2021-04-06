class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum=[]
        x=0
        for i in nums:
            x=x+i
            runsum.append(x)
        return runsum