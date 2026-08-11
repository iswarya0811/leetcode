class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max:
                max = i - min_price
                
 
        return max

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna