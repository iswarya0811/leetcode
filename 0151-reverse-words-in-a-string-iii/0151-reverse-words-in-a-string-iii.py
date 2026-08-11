class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        t =''
        for i in s:
            t += i[::-1]
            t+=' '
        return t.strip()
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna