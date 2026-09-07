class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        current_v = sum(1 for i in range(k) if s[i] in vowels)
        max_v = current_v
        for i in range(k,len(s)):
            if s[i] in vowels:
                current_v +=1
            if s[i-k] in vowels:
                current_v -= 1
            if current_v >=max_v:
                max_v = current_v
        return max_v

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna