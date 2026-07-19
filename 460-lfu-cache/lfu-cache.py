class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.time = 0
        self.heap = [] #stores node([freq, tick, key, value]), sorts on freq, min heap
        self.cache = {} #stores key -> node

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.cache:
            self.cache[key][0] += 1 #update freq
            self.cache[key][1] = self.time #update time
            heapq.heapify(self.heap)
            return self.cache[key][3] #return val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.cache:
            self.cache[key][0] += 1 #update freq
            self.cache[key][1] = self.time #update time
            self.cache[key][3] = value #update val
            heapq.heapify(self.heap)
        else:
            if self.capacity == len(self.cache):
                node = heapq.heappop(self.heap)
                self.cache.pop(node[2])
            node = [1, self.time, key, value]
            self.cache[key] = node
            heapq.heappush(self.heap, node)



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)