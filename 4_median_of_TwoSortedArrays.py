class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=sorted(nums1 + nums2)
        left=0
        right=len(nums3)-1
        if len(nums3)%2!=0:
            return float(nums3[(left+right)//2])
        else:
            mid1=nums3[(left+right)//2] 
            mid2=nums3[(left+right)//2+1] 
            return (mid1+mid2)/2