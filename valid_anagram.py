class Solution():   
    def validAnagram(self, s,t) -> bool:
        # return sorted(str1)==sorted(str2)
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1

        return True
        
array=Solution()
print(array.validAnagram("rose","sore"))
