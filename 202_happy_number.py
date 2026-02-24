class Solution:
    # def isHappy(self, n: int,seen=None) -> bool:
    #     if seen is None:
    #         seen=set()
    #     sum_q=0
        
    #     if(n == 1):
    #         return True
        
    #     if n in seen:
    #         return False
        
    #     seen.add(n)

    #     while n>0:
            
    #         digit=n%10
    #         sum_q+=digit**2
    #         n=n//10
    #     return self.isHappy(sum_q,seen) 
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            # compute sum of squares
            n = sum(int(d)**2 for d in str(n))

        return True


    
array=Solution()
print(array.isHappy(19))