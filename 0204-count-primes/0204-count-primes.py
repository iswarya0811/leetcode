class Solution:
    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0
        prime=[True]*n
        prime[0]=False
        prime[1]=False
        p=2
        while p*p<n:
            if prime[p]:
                for m in range(p*p,n,p):
                    prime[m]=False
            p=p+1
        c=0
        for i in range(n):
            if prime[i]:
                c+=1
        return c
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna