class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        max_so_far = 0
        
        for i, val in enumerate(arr):
            max_so_far = max(max_so_far, val)
            
            if max_so_far == i:
                chunks += 1
                
        return chunks


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna