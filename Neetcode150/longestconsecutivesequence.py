class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        maxlength = 1
        for num in numset:
            length = 1
            if (num-1) in numset:
                continue
            while (num+length) in numset:
                length += 1
            maxlength = max(maxlength, length)
        return maxlength

 
list = [1,2,9,7,8]
A = Solution()
print(A.longestConsecutive(list))