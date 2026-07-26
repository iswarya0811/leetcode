class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxi = 0
        while left < right:
            width = right - left
            length = min(height[left],height[right])
            area = width*length
            if area > maxi:
                maxi = area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maxi
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna