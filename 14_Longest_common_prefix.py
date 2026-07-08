class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix=strs[0]
        for str in strs:
            while str.startswith(prefix)==False:
                prefix=prefix[:-1]
        return prefix