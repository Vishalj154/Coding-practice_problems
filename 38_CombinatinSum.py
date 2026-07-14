class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
       
        def backtrack(index, remaining, combination):
            if remaining==0:
                result.append(combination[:])
                return
            if remaining<0:
                return
            for i in range(index,len(candidates)):
                combination.append(candidates[i])
                backtrack(i,remaining-candidates[i],combination)
                combination.pop()
        backtrack(0,target,[])
        return result