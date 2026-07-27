class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = nums[0]
        ms = nums[0]
        for i in range(1,len(nums)):
            cs = max(nums[i],cs+nums[i])
            ms = max(cs,ms)
        return ms
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna