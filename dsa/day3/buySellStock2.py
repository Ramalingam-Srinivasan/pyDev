#122. Best Time to Buy and Sell Stock II

class Solution(object):
    def maxProfit(self,prices):
        max_profit = 0

        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the price has increased, add the difference to max_profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        # Return the total profit
        return max_profit
        