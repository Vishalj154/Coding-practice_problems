class Solution:
    def findDuplicates(self, nums):
        
        seen = set()
        dup = []

        for num in nums:
            if num in seen:
                dup.append(num)
            else:
                seen.add(num)

        return dup

array=Solution()
print(array.findDuplicates([2,4,6,5,2]))
               


        