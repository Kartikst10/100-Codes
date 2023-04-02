#https://leetcode.com/problems/two-sum/
from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i,n in enumerate(nums):
            if target - n in hashset:
                return [hashset[target-n],i]
            hashset[n] = i