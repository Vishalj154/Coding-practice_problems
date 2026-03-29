class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        give = 1
        i = 0
        
        while candies > 0:
            person = i % num_people
            give_amt = min(give, candies)
            
            res[person] += give_amt
            candies -= give_amt
            
            give += 1
            i += 1
        
        return res
    
candy=Solution()
print(candy.distributeCandies(1000, 4))