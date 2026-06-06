class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: (x[0], x[1]), reverse=True)
        stack = []
        res = 0
        curr_time = -1

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > curr_time:
                res += 1
                curr_time = time
        return res