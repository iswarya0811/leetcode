class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        return (nums[size-1]-1)*(nums[size-2]-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna