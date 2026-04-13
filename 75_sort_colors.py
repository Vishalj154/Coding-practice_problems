class Solution:
    def sortcolors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[j] < nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
            
        
        print(nums)
            
        
       
            
        
const=Solution()  
const.sortcolors([2,0,2,1,1,0])