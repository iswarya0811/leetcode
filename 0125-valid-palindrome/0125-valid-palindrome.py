class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = [char.lower() for char in s if char.isalnum()]
        return cleaned_chars == cleaned_chars[::-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna