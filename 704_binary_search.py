class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        while low < high:
            mid=(low+high)//2
            

