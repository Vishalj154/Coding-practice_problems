class Solution:
    def sortcolors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        mid=0
        while mid<=high :
            if(nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            elif(nums[mid]==2):
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            
        print (nums)
       
            
        
const=Solution()  
const.sortcolors([2,0,2,1,1,0])