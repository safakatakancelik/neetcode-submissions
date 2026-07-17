class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        simple and beautiful
        """
        # keep track of lowest price and the max profits
        lowest_so_far = prices[0]
        max_profit_so_far = 0

        # loop through each price
        for price in prices:
            # keep the records up to date
            lowest_so_far = min(price, lowest_so_far)
            max_profit_so_far = max(price - lowest_so_far, max_profit_so_far)
            
        return max_profit_so_far