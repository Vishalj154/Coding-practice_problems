class Solution:
    def sortcolors(self, nums,low,high) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        def partition(self,nums,low,high):
            pi=len(nums)-1
            i=low-1
            for j in range (low,high):
                if(nums[j]<nums[pi]):
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]
            nums[i+1],nums[pi]=nums[pi],nums[i+1]
            return i+1
        if(low < high):
            pi=partition(self,nums,low,high)
            self.sortcolors(nums,low,pi-1)
            self.sortcolors(nums,pi+1,high)
        
        print(nums)
            
        
       
            
        
const=Solution()  
const.sortcolors([2,0,2,1,1,0],0,len([2,0,2,1,1,0])-1)