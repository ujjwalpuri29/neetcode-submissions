class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        res = 0
        l, r = 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            
            if time > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res