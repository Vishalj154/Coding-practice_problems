class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        def merge(a,b):
            return int(str(a)+str(b))

        ans=float("inf")

        for i in range(0,len(nums)-1,2):
            c=merge(nums[i],nums[i+1])
            ans=min(ans,c)
        return ans