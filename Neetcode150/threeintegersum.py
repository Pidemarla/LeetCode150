class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result =[]
        i = 0
        while i < len(nums)-1:
            while nums[i] == nums[i-1]:
                i = i+1
            L = i+1
            R = len(nums)-1
            while L < R:
                while L<R and nums[L] == nums[L+1]:
                    L +=1
                while L<R and nums[R] == nums[R-1]:
                    R -=1
                threesum = nums[i] + nums[L] + nums[R]
                if L < R and threesum == 0:
                    result.append([nums[i],nums[L],nums[R]])
                    L +=1
                    R -=1
                elif L < R and threesum < 0:
                    L +=1
                else:
                    R -=1
            i =i+1
        return result
                
 
A = Solution()
list = [-1,0,1,2,-1,-4]
print(A.threeSum(list))