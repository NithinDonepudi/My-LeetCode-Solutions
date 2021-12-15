class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for i in range(k):
            nums.insert(i,nums[len(nums)-k+i])
        for i in range(k):
            nums.pop()
