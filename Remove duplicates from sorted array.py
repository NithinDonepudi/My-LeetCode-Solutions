class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i=i+1
        return len(nums)
            
        