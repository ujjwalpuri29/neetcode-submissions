class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = set(nums)
        seen = defaultdict(int)
        for i in nums:
            seen[i] = 1 + seen[i-1] + seen[i+1]
            seen[i-seen[i-1]] = seen[i]
            seen[i+seen[i+1]] = seen[i]
        
        return max(seen.values())