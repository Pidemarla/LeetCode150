class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count ={}
        freq = [[] for i in range(len(nums))]
        for num in nums:
            count[num] = 1+ count.get(num,0)
        for num,cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1, -1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

A = Solution()
list1 = [1,5,5,5,9,9,9,9]
k =2
print(A.topKFrequent(list1,k))