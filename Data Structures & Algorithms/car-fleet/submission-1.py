class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position = sorted(zip(position, speed), key=lambda x: (x[0], x[1]), reverse=True)
        stack = []
        res = 0

        for pos, sp in sorted_position:
            time = (target - pos) / sp
            if not stack or stack[-1] < time:
                res += 1
                stack.append(time)
        return res