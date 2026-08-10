class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect if a cycle exists and find the intersection point
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]          # Moves 1 step
            hare = nums[nums[hare]]            # Moves 2 steps
            if tortoise == hare:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]          # Moves 1 step
            hare = nums[hare]                  # Moves 1 step
            
        return hare


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna