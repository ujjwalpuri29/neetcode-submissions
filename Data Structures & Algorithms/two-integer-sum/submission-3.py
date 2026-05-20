class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}
        for i, num in enumerate(nums):
            if target - num in present:
                return [present[target - num], i]
            present[num] = i