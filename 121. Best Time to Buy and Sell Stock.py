class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: sliding window
        left = right = 0
        result = 0
        while right < len(prices):
            if prices[right] - prices[left] >= 0:
                temp = prices[right] - prices[left]
                result = max(result, temp)
            else:
                left = right
            right += 1
        return result