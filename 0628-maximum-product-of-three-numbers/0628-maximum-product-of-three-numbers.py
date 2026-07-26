class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        return max(nums[size-1]*nums[size-2]*nums[size-3],nums[0]*nums[1]*nums[size-1])
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna