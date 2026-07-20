def sum(n):
    s=0
    while n>0:
        s=s+((n%10)*(n%10))
        n=n//10
    return s
class Solution:
   
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n!=1 and n not in seen:
            seen.add(n)
            n = sum(n)
        return n==1
         
          

        
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna