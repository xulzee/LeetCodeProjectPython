import collections


class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == '__main__':
    # inputs:
    # ["RecentCounter", "ping", "ping", "ping", "ping"]
    # [[], [1], [100], [3001], [3002]]
    # [null, 1, 2, 3, 3]
    obj = RecentCounter()
    print(obj.ping(1), obj.ping(100), obj.ping(3001), obj.ping(3002))
