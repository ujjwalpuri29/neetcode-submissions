class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while st and st[-1][0] < temp:
                a, res_idx = st.pop()
                res[res_idx] = idx - res_idx
            st.append((temp, idx))
        return res