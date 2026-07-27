class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        exsum = n * (n+1) //2
        acsum = sum(nums)
        seen = set()
        for i in nums:
            if i in seen:
                dup = i
                break
            seen.add(i)
        missing = exsum-(acsum-dup)
        return [dup,missing]
              
        

        
       
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna