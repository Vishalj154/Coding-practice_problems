class Solution:
    def fib(self, n: int) -> int:
        f=[0]*3
        f[0]=0
        f[1]=1
        if(n==1 or n==0):
                return n
        for i in range(2,n+1):
            f[2]=f[1]+f[0]
            f[0]=f[1]
            f[1]=f[2]
        return f[2]