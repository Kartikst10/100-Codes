# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        L = set(nums)
        longest = 0
        for n in nums:    
            if (n-1) not in L:
                length = 1
                while(n+length) in L:
                    #n+=length
                    length+=1
                longest = max(length,longest)
        return longest