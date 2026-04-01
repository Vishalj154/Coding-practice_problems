class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # last index of nums1 valid part
        j = n - 1  # last index of nums2
        k = m + n - 1  # last index of nums1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 still has elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1

ar=[1,2,3,0,0,0]
ar2=[2,4,5,6]
c=Solution()
print(c.merge(ar,3,ar2,3))