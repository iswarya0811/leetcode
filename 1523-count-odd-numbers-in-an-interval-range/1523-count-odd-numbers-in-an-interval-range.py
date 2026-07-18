class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt=0
        if low%2!=0:
            cnt+=1
        if high%2!=0:
            cnt+=1
        ans =int((high-low)//2)
        if(cnt!=0):
            return ans+1
        else:
            return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna