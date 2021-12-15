class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        intersection=[]
        for value in set1:
            if value in set2:
                for i in range(min(nums1.count(value),nums2.count(value))):
                    intersection.append(value)
        return intersection
