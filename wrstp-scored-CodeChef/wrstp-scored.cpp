# cook your dish here
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        # Count the occurrences of each movement
        x = s.count('R') - s.count('L')
        y = s.count('U') - s.count('D')
        
        # Check if the final position is exactly one flip away from (0, 0)
        if (x == 0 and abs(y) == 2) or (abs(x) == 2 and y == 0):
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna