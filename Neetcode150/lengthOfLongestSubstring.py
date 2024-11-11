class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        L = 0
        charset = set()

        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[L])
                L +=1
            charset.add(s[R])
            result = max(result,R-L+1)
        return result
A =Solution()
s = "zxyzxyz"
print(A.lengthOfLongestSubstring(s))