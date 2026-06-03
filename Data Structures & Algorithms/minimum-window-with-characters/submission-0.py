class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        
        have, need = 0, len(countT)
        l = 0
        window = {}
        res = [-1, -1]
        reslen = float('inf')

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if reslen != float('inf') else ""
                
