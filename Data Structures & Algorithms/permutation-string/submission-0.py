class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1
        
        l = 0

        while l < len(s2) - len(s1) + 1:
            if s2[l] in freq:
                freq2 = {}
                for r in range(l, l + len(s1)):
                    freq2[s2[r]] = freq2.get(s2[r], 0) + 1
                if freq == freq2:
                    return True
            l += 1
        return False