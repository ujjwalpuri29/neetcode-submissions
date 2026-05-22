class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [str(len(word)) for word in strs]
        encoded_string = ",".join(lens) + "#" + "".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []

        lens, strs = s.split("#", 1)
        lens = lens.split(",")

        start = 0
        res = []
        for length in lens:
            end = start + int(length)
            word = strs[start : end]
            res.append(word)
            start = end
        return res