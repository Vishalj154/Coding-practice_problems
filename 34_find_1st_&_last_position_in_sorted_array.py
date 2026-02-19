from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]

        low = 0
        high = len(nums) - 1

        def first(nums, target, low, high):
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    ans = mid
                    high = mid - 1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        def last(nums, target, low, high):
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    ans = mid
                    low = mid + 1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        return [first(nums, target, low, high),
                last(nums, target, low, high)]
