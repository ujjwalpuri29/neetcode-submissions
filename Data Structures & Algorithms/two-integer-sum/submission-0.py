class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}
        for i, num in enumerate(nums):
            if target - num not in present:
                present[num] = i
            else:
                return [present[target - num], i]
            print(present)
        return -1