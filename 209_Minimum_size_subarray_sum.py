class Solution:
    def minSubArrayLen(self, target: int, nums) :
        left = 0
        curr_sum = 0
        ans=float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                length=right-left+1
                # if length < ans:
                #     ans=length
                ans=min(length,ans)
                # update answer
                curr_sum -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0
        return ans
        