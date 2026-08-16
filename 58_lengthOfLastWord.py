class Solution:
    def lengthOfLastWord(self, s) -> int:
        s=s.split( )
        return len(s[-1])

c=Solution()
print(c.lengthOfLastWord("Hello World"))