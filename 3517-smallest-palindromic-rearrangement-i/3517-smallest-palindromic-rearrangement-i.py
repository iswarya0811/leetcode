class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans = ""
        middle=""
        for k,v in sorted(freq.items()):
            ans+=(floor(v/2)*k)
            if v%2!=0:
                middle+=k
        return ans+middle+ans[::-1]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna