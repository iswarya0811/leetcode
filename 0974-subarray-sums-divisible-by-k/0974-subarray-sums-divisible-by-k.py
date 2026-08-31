class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dicti = {0:1}
        prefix_lst = [nums[0]]
        sum = nums[0]
        for i in range(1,len(nums)):
            sum+=nums[i]
            prefix_lst.append(sum)
        count = 0
        for i in prefix_lst:
            rem = i%k
            if rem in dicti:
                count += dicti[rem]
                dicti[rem]+=1
            else:
                dicti[rem]=1
        return count

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna