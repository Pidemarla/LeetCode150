class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        
        #Using Hash Set Length
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
        #Using Hash Set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
        #Brute Force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
        #using Sorting
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
     
arr=[1,2,3,4,4]
a = Solution()
hasDuplicate = a.hasDuplicate(arr)
print("Contains duplicate:", hasDuplicate)