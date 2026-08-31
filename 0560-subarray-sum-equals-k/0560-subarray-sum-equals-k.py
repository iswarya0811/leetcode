class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dicti = {}
        prefix_lst = [nums[0]]
        sum= nums[0]
        for i in range(1,len(nums)):
            sum += nums[i]
            prefix_lst.append(sum)
        count = 0
        for i in prefix_lst:
            if i == k:
                count+=1
            if i-k in dicti:
                count += dicti[i-k]
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
        return count



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna