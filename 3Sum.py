# https://leetcode.com/problems/3sum/
class Solution:
    def ThreeSum(self, integers):
        """
        :type integers: List[int]
        :rtype: List[List[int]]
        """
        integers.sort()
        result = []
        for index in range(len(integers)):
            if integers[index] > 0:
                break
            if index > 0 and integers[index] == integers[index - 1]:
                continue
            left, right = index + 1, len(integers) - 1
            while left < right:
                if integers[left] + integers[right] < 0 - integers[index]:
                    left += 1
                elif integers[left] + integers[right] > 0 - integers[index]:
                    right -= 1
                else:
                    result.append([integers[index], integers[left], integers[right]])
                    left += 1 
                    right -= 1 
                    while integers[left] == integers[left - 1] and left < right:
                        left += 1 
        return result
