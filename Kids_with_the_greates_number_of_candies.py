class Solution:
    def kidsWithCandies(self, candies,  extraCandies: int):
        result = []
        largest = max(candies)
        
        for i in candies:

            if i + extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)
        
        return result
