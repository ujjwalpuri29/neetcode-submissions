class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        lprefix = [height[0]]
        for i in range(1, len(height)):
            lprefix.append(max(lprefix[-1], height[i]))
        
        rprefix = [height[-1]]
        for i in range(len(height) - 2, -1, -1):
            rprefix.append(max(rprefix[-1], height[i]))

        rprefix = rprefix[::-1]

        water = 0
        for i in range(len(height)):
            water += min(lprefix[i], rprefix[i]) - height[i]
        
        return water