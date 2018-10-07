# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you
# like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell
# the stock before you buy again).
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# Input: [7,1,5,3,6,4]
# We'll be using the peaks-and-valleys approach.
# If you plot these numbers in a graph, you will have:
# A peak of 7 at the start.
# A valley of 1
# A peak of 5
# A valley of 3
# A peak of 6
# A valley of 4
# The idea is to always consider every peak immediately following a valley to maximize the profit.
# In this case, we need to consider buying in the valleys of 1 and 1 and 3 to sell in their consecutive peaks.
# Total time complexity: O(n)

class Solution:
    def get_minimum_valley(self, prices, i):
        while i < (len(prices) - 1) and (prices[i] >= prices[i+1]):
            i += 1
        valley = prices[i]
        return valley, i

    def get_maximum_peak(self, prices, i):
        while i < (len(prices) - 1) and prices[i] <= prices[i+1]:
            i += 1
        peak = prices[i]
        return peak, i

    def get_maximum_peak_and_valley_profit_margin(self, prices, i):
        valley, i = self.get_minimum_valley(prices, i)
        peak, i = self.get_maximum_peak(prices, i)
        return peak-valley, i

    def cannot_make_profit_with(self, prices):
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                return False
        return True

    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0 or self.cannot_make_profit_with(prices):
            return 0
        i = max_profit = 0
        while i < (len(prices) - 1):
            profit_margin, i = self.get_maximum_peak_and_valley_profit_margin(prices, i)
            max_profit += profit_margin
        return max_profit

