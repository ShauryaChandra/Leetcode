#using Set

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()

#         for num in nums:
#             if num in seen:
#                 return True
            
#             seen.add(num)
        
#         return False

# Using Dict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            
            # seen.add(num) -> works only for Sets, not for Dict
            seen[num] = 1       # to store a number in dict (value can be anything there (1,0,56,True,etc))

        return False