class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)
        return countS == countT


        count = [0] * 26
        for i in range(len(s)):
            # ord is used to get the unicode value of the character like ord(a) = 97 so 
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

        s = sorted(s)
        t = sorted(t)
        if s==t:
            return True
        else:
            return False

A = Solution()
s = "anagram"
t = "anagram"
print(A.isAnagram(s,t))