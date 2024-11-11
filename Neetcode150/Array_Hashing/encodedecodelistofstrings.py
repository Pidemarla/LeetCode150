class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for str in strs:
            result = f"{result}" + f"{len(str)}#{str}"
        return result
                                 
    def decode(self, s: str) -> list[str]:
        list =[]
        i = 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j = j+1
            length =int(s[i:j])
            i = j+1
            j = i+ length
            list.append(s[i:j])
            i = j
        return list
A = Solution()
list1 = ["abcd","efg","hijkl"]
encoded = A.encode(list1)
print(encoded)
decoded = A.decode(encoded)
print(decoded)