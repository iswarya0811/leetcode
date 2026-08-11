class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(0,len(nums),2):
            cnt += min(nums[i],nums[i+1])
        return cnt
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna