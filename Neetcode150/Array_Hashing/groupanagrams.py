from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return res.values()
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) -ord('a')] +=1
            res[tuple(count)].append(s)
        return res.values()
    
A = Solution()
list1 = ["ant","nat","cat"]
groupAnagrams = A.groupAnagrams(list1)
print(groupAnagrams)
