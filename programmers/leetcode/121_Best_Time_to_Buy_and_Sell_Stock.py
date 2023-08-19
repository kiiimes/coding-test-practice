class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        total = 0

        for i in range(len(prices)-1,0,-1):
            if max_num < prices[i]:
                max_num = prices[i]
            temp = max_num - prices[i-1]
            if total < temp:
                total = temp

        return total

