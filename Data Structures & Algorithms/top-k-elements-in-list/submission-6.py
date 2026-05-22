class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in freq:
            buckets[freq[num]].append(num)
        
        res = []
        for i in range(len(buckets) -1, -1, -1):
            if len(res) >= k:
                return res[:k]            
            res.extend(buckets[i])
