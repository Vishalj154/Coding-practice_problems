class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        # Append any remaining elements from either array
        nums3.extend(nums1[i:])
        nums3.extend(nums2[j:])
        left=0
        right=len(nums3)-1
        if len(nums3)%2!=0:
            return float(nums3[(left+right)//2])
        else:
            mid1=nums3[(left+right)//2] 
            mid2=nums3[(left+right)//2+1] 
            return (mid1+mid2)/2