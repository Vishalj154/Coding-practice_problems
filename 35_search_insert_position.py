class Solution:
    def searchInsert(self, nums , target: int) -> int:
        low=0
        high=len(nums)-1
        while low <= high:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid-1
            elif target < nums[mid] and target > nums[mid-1]:
                return mid
            elif target > nums[mid] and target < nums[mid+1]:
                return mid+1
            elif target < nums[mid]:
                high=mid-1
