class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        if ruleKey == "color":
            index = 1
        if ruleKey == "name":
            index = 2
        cnt = 0
        for i in items:
            if i[index] == ruleValue:
                cnt+=1
        return cnt
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna