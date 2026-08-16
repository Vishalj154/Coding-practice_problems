class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=list(map(split(",")))
        return len(s[-1])