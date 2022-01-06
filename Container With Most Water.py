class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height)-1
        while l < r:
            distance = r - l
            minWall = min(height[l], height[r])
            area = minWall * distance
            if area > maxArea:
                maxArea = area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxArea
