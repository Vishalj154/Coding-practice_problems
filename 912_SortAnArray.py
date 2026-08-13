class Solution:
    def sortArray(self, nums) :
        

        def merge(nums,p,q,r):
            n1=q-p+1
            n2=r-q
            L=[0]*(n1+1)
            R=[0]*(n2+1)
            for i in range(0,n1):
                L[i]=nums[p+i]
            for j in range(0,n2):
                R[j]=nums[q+1+j]
            L[n1]=float('inf')
            R[n2]=float('inf')
            i=0
            j=0
            for k in range(p,r+1):
                if L[i]<=R[j]:
                    nums[k]=L[i]
                    i=i+1
                else:
                    nums[k]=R[j]
                    j=j+1

        def mergesort(nums,p,r):
            if p < r:
                q=(p+r)//2
                mergesort(nums,p,q)
                mergesort(nums,q+1,r)
                merge(nums,p,q,r)
        mergesort(nums, 0, len(nums) - 1)

        return nums
    
c=Solution()
print(c.sortArray([5,2,3,1]))
        
                

