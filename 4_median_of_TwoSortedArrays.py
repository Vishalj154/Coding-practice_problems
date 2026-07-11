class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1 + nums2
        if len(nums3)%2!=0:
            
        return (max(nums3)+min(nums3))/2