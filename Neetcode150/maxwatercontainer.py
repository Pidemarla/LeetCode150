class Solution:
    def maxArea(self, heights: list[int]) -> int:
        if not heights or len(heights) == 1:
            return 0
        L = 0
        R = len(heights)-1
        maxarea = 1
        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            maxarea = max(maxarea,area)
            if height[L] < heights[R]:
                L +=1
            else:
                R -=1
        return maxarea

A = Solution()
height = [2,2,2]
print(A.maxArea(height))