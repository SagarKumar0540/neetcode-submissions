class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        values = self.store.get(key,[])
        low = 0
        high = len(values)-1

        while low<=high:
            mid = (low+high) // 2

            if values[mid][0] <= timestamp:
                ans = values[mid][1]
                low = mid +1
            else:
                high = mid -1
        return ans
        
