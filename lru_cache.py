# 146. LRU Cache
from collections import deque


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.m:
            if len(self.deq) == self.capacity:
                old = self.deq.popleft()
                del self.m[old]
        else:
            self.deq.remove(key)
        self.m[key] = value
        self.deq.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
