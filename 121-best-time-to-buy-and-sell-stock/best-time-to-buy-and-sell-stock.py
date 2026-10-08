class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        n = len(prices)
        for i in range(n):
            cost = prices[i] - mini
            maxi = max(maxi,cost)
            mini = min(mini,prices[i])
        return maxi
    