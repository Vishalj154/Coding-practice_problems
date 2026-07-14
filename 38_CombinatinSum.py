class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        s=[]
        for num in candiadtes:
            if target%num==0:
                q=target//num
                s.append([num]*q)
        i=0
        while i<len(nums):
            q=target-candidates[i]
            if q in candidates:
                s.join([candidates[i],q])