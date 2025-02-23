#121. Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self,prices):
    # Initialize variables
            min_price = float('inf')  # Set to a very large value
            max_profit = 0

            # Iterate through the prices
            for price in prices:
                # Update min_price if the current price is lower
                if price < min_price:
                    min_price = price
                # Calculate the current profit
                current_profit = price - min_price
                # Update max_profit if the current profit is greater
                if current_profit > max_profit:
                    max_profit = current_profit

            # Return the maximum profit
            return max_profit