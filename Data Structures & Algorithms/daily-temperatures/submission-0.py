class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((temp, i))
            print(stack)
            print(res)
        return res