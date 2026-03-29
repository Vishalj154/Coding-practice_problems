class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        if(n==1 or n==2):
            return 1
        elif(n==0):
            return 0
        for i in range(3,n+1):
            d=a+b+c
            a=b
            b=c
            c=d

        return d
    
fibo=Solution()
print(fibo.tribonacci(45))