class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in nums1:
            j = nums2.index(i)
            max = -1
            for k in range(j,len(nums2)):
                if nums2[k]>i :
                    max = nums2[k]
                    break
            lst.append(max)
        return lst
                    

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna