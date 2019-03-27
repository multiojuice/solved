"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Owen Sullivan
Should be O(N)
Runtime: 40 ms, faster than 99.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.9 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 9999999999
        difference = 0
        for price in prices:
            if price < low:
                low = price
            if price - low > difference:
                difference = price - low

        return difference

