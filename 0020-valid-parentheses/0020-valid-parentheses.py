class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracs=['(','[','{']
        mappings = {')':'(','}':'{',']':'['}
        for i in s:
            if i in open_bracs:
                stack.append(i)
            else:
                if not stack or stack[-1]!=mappings[i]:
                    return False
                stack.pop()
        return len(stack)==0




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna