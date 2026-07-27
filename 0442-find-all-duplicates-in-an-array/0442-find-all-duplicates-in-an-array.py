class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        ans =[]
        for i in nums:
            if i  in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        for k,v in freq.items():
            if v==2:
                ans.append(k)
        return ans





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna