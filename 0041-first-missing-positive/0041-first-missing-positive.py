class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        num=1
        while True:
            if num in s:
                num+=1
            else:
                return num
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna