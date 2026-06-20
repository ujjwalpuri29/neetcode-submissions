class TimeMap:

    def __init__(self):
        self.kv_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv_map:
            self.kv_map[key].append((timestamp, value))
        else:
            self.kv_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_map:
            return ""

        if timestamp > self.kv_map[key][-1][0]:
            return self.kv_map[key][-1][1]
        elif timestamp < self.kv_map[key][0][0]:
            return ""
            
        l, r = 0, len(self.kv_map[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            
            if self.kv_map[key][m][0] == timestamp:
                return self.kv_map[key][m][1]
            elif self.kv_map[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return self.kv_map[key][r][1]
        
