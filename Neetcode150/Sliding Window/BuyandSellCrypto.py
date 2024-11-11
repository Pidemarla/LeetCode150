class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L,R = 0,1
        maxprofit = 0

        while R < len(prices):
            profit = prices[R] - prices[L]
            maxprofit = max(maxprofit,profit)
            if prices[L] > prices[R]:
                L = R
                R +=1
            else:
                R= R+1
        return maxprofit

A = Solution()
prices = [0,8,78,0,555]
print(A.maxProfit(prices))