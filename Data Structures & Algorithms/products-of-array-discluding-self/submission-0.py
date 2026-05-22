class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(nums[i-1] * res[-1])

        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp *= nums[i + 1]
            res[i] *= temp        
        return res