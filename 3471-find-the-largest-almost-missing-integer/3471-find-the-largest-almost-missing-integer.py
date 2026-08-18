class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n= len(nums)
        if k==n:
            return max(nums)
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        if k==1:
            ans = -1
            for k,v in freq.items():
                if v==1:
                    ans = max(ans,k)
            return ans
        first = nums[0]
        last = nums[len(nums)-1]
        maxi=-1
        for k,v in freq.items():
            if v==1 and (k==first or k==last):
                if k>=maxi:
                    maxi=k
        return maxi
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna