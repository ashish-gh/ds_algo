# 1.4. Finding the Largest or Smallest N Items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(2, nums))

heap = list(nums)
heapq.heapify(heap)
print(heap[:2])

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(sorted(nums, reverse=False)[:2])


# 1.5. Implementing a Priority Queue
# You want to implement a queue that sorts items by a given priority and always returns
# the item with the highest priority on each pop operation.


class Item:
    def __init__(self, name) -> None:
        self.name = name


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self._index = 0

    def push(self, item: Item, priority: int = 0):
        self.queue.append([item, priority])

    def pop(self):
        if not self.queue:
            return []
        return sorted(self.queue, key=lambda x: x[1])[-1]


import heapq


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self._index = 0

    def push(self, item: Item, priority: int):
        heapq.heappush(self.queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


q = PriorityQueue()
q.push(Item("foo"), 5)
print(q.pop())


# 1.13. Sorting a List of Dictionaries by a Common Key


from operator import itemgetter

rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
]

print(sorted(rows, key=itemgetter("fname")))

