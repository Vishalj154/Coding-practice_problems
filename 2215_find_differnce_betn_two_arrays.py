class Solution:
    def intersection(self, nums1, nums2):
            for1=[]
            for2=[]
            for num in nums1:
                  if num not in nums2:
                        for1.append(num)
            for num in nums2:
                  if num not in nums1:
                        for2.append(num)
            return [list(set(for1)),list(set(for2))]
            