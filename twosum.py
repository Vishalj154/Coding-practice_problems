import ast

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i



nums = ast.literal_eval(input())
target = int(input())

obj = Solution()
result = obj.twoSum(nums, target)
print(result)
