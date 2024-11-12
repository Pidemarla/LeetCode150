class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        count = {}
        maxf = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R],0)
            maxf = max(maxf, count[s[R]])
            # while (R-L+1) - max(count.values()) > k:
            while (R-L+1) - maxf > k:
                count[s[L]] -= 1
                L +=1
            res = max(res, R-L+1)
        return res
A = Solution()
s = "XYYX"
k = 2
print(A.characterReplacement(s,k))