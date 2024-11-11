class Solution:
    def trap(self, height: list[int]) -> int:
        L,R =0,len(height)-1
        maxleft,maxright = height[L],height[R]
        result = 0
        while L<R:
            if maxleft < maxright:
                L = L+1
                if height[L] < maxleft:
                    result += maxleft -height[L]
                else:
                    maxleft = height[L]
            else:
                R = R-1
                if height[R] < maxright:
                    result += maxright -height[R]
                else:
                    maxright = height[R]
        return result

A = Solution()
height = [1,0,3,0,1,0,2,0,5]
print(A.trap(height))