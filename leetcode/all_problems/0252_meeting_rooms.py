from typing import List


class Intervals:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class Solution:
    def meeting_rooms(self, intervals: List[Intervals]):
        intervals.sort(key=lambda x: x.start) 
        for i in range(1, len(intervals)):
            interval1 = intervals[i-1]
            interval2 = intervals[i]
            if interval1.end > interval2.start:
                return False
        return True



def main():
    intervals = [(0,30),(5,10),(15,20)]
    intervals = [(1,4), (4,10), (23,24)]
    intervals = [Intervals(i[0], i[1]) for i in intervals]
    sl = Solution()
    print(sl.meeting_rooms(intervals))

if __name__ == "__main__":
    main()
