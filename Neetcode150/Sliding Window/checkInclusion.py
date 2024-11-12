class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)
        return countS == countT
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        L = 0
        for R in range(len(s1)-1, len(s2)):
            print(s2[L:R])
            if self.isAnagram(s1, s2[L:R+1]):
                return True
            else:
                L +=1
        return False
        
A = Solution()
s1 = "abc" 
s2 = "lecebecab"
print(A.checkInclusion(s1,s2))