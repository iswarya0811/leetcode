class Solution:
    def countCommas(self, n: int) -> int:

        length =  len(str(n))
        cnt = 0
        if length > 3:
            cnt += (n-999)
        return cnt
            
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna