class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for j in range(len(nums)):
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i=i+1
        return len(nums)