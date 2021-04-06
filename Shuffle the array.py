class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle=[]
        for i in range(int((len(nums)+1)/2)):
            shuffle.append(nums[i])
            shuffle.append(nums[int((len(nums)+1)/2)+i])
        return shuffle