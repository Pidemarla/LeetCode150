from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        count = defaultdict(int)
        window = defaultdict(int)
        for i in range(len(t)):
            count[t[i]] += 1 
        need = len(count)
        have = 0
        res ,reslen = [-1,-1] , float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            if count[c] !=0:
                window[c] +=1
                if window[c] == count[c]:
                    have +=1
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                if count[s[l]] == 0:
                    l +=1
                else:
                    window[s[l]] -=1
                    if window[s[l]] < count[s[l]]:
                        have -= 1
                        l +=1
                    
        return s[res[0]:res[1]+1]

A = Solution()
s1 = "x" 
s2 = "xy"
print(A.minWindow(s1,s2))