class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while i*i  <= x:
            i+=1

        print(i-1)
    
c=Solution()
c.mySqrt(1098756)