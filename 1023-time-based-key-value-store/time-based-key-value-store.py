from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(lambda: defaultdict(int))
        self.timestamps = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.hashmap) or len(self.timestamps) == 0:
            return ""
        if timestamp in self.hashmap[key]:
            return self.hashmap[key][timestamp]
        return self.binarySearch(key, timestamp)
    
    def binarySearch(self, key, timestamp):
        maxTime = -1
        start, end = 0, len(self.timestamps[key])-1

        while end >= start:
            mid = (start+end)//2
            if self.timestamps[key][mid] > timestamp:
                end = mid-1
            else:
                maxTime = max(maxTime, self.timestamps[key][mid])
                start = mid+1

        return self.hashmap[key][maxTime] if maxTime > -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)