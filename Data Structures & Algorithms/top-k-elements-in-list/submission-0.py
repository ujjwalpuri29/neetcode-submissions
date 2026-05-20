class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
        print(sorted_freq)

        res = []
        for i in range(k):
            res.append(sorted_freq[i][0])
        
        return res