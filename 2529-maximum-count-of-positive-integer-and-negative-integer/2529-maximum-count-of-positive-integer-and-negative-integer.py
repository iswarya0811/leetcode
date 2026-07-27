class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,n=0,0
        for i in nums:
            if i > 0 :
                p+=1
            if i < 0:
                n+=1
        return max(p,n)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna