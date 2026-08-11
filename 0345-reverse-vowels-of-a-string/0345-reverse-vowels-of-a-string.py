class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        v = set("aeiouAEIOU")
        i = 0
        j = len(s)-1
        while i < j:
            if a[i] not in v:
                i+=1
            elif a[j] not in v:
                j-=1
            else:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
        return "".join(a)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna