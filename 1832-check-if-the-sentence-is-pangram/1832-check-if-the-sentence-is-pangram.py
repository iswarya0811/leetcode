class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst = [0]*26
        for i in sentence:
            index = ord(i)-ord('a')
            lst[index]+=1
        for i in lst:
            if i==0:
                return False
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna