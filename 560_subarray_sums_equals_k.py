class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left=0
        curr_sum=0
        count=0
        for right in range(len(nums)):
            curr_sum+=nums[right]

            while curr_sum == k:
                count+=1
                
