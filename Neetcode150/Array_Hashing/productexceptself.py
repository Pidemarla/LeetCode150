class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix =1
        postfix = 1
        output = [ [] for i in range(len(nums)) ]
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = prefix * nums[i-1] 
            prefix = prefix * output[i]
        for j in range(len(nums)-2, -1,-1):
            postfix = postfix * nums[j+1]
            output[j] = postfix * output[j]
        return output

numbers = [1,2,4,6]
A = Solution()
print(A.productExceptSelf(numbers))