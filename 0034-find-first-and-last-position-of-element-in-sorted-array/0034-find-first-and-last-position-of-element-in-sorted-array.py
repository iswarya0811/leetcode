def BinarySearch(nums,target):
    low = 0
    high = len(nums)-1
    ans = []
    first = -1
    last =-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            first = mid
            high = mid-1
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    low = 0
    high = len(nums)-1
    
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            last=mid
            low = mid+1
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid -1
    ans.append(first)
    ans.append(last)
    return ans

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return BinarySearch(nums,target)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna