#1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = []
        all_sum = 0
        for z in range(len(nums)):
            all_sum += nums[z]
            nums[z] = all_sum
        return nums
