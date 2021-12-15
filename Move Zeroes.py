class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num=nums.count(0)
        for i in range(num):
            nums.remove(0)
            nums.append(0)
        return nums
