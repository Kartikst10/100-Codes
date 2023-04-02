# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1

        for i in range(len(nums)):
            res.append(pre)
            pre*=nums[i]
        #eturn res
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *=post 
            post *= nums[i]
            #print("hi",post)
            
            #print("h",res[i-1])
        return res