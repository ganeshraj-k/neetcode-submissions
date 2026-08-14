class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minprice = prices[0]

        for sell in prices:
            maxp = max(maxp, sell-minprice)

            minprice = min(minprice, sell)

        return maxp