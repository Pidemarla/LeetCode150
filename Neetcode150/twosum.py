class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        preHashmap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in preHashmap:
                return [preHashmap[diff], i]
            else:
                preHashmap[n] = i
        
        #Brute Force
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        

A = Solution()
list1 = [1,5,7,9]
target = 10
twoSum = A.twoSum(list1,target)
print(twoSum)