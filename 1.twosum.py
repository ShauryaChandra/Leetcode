# # BRUTE FORCE
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# Dictionary solution
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            need = target - nums[i]         # find the number needed to reach the target

            if need in seen:                # if needed number already exists or not
                return [seen[need], i]      # returns index of needed number and current index

            seen[nums[i]] = i               # store current number and its index