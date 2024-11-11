from collections import defaultdict
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L,R= 0, len(numbers)-1
        sum = 0
        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L+1,R+1]
            if sum < target:
                L +=1
            else:
                R -=1
        return []
    def twoSumUsingHashmap(self, numbers: list[int], target: int) -> list[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if mp[temp]:
                return [mp[temp], i+1]
            else:
                mp[numbers[i]] = i+1
        return []
A = Solution()
list = [1,2,3,4,7]
target = 9
print(A.twoSumUsingHashmap(list,target))