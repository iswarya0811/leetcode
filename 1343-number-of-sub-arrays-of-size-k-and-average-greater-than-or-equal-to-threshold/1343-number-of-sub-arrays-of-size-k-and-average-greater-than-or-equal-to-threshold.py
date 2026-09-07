class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        cnt =0
        for i in range(k,len(arr)):
            if current_sum>=(k*threshold):
                cnt+=1
            current_sum+=arr[i]
            current_sum-=arr[i-k]
        if current_sum>=(k*threshold):
            cnt+=1
        return cnt
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna