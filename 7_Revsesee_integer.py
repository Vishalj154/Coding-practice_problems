class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        y=0
        while x !=0:
            remain=x%10
            y=(y*10)+remain
            x=x//10

        y*=sign
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y
        
    
c=Solution()
print(c.reverse(-123))
