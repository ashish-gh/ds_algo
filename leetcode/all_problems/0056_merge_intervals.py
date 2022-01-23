# Time complexity: O(n logn ) n: number of intervals

from typing import List


class Solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        # pythonic way of sorting intervals 
        # implements merge sort
        intervals.sort(key= lambda x: x[0])
        # getting the first element of the sorted list to avoid the edge case
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # from the output get the most recent added intervals
            last_end = output[-1][1]
            if start <= last_end:
                # this means they are overlapping 
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output



def main():
    list = [[1,4],[2,6],[15,20],[8,10]]
    sl = Solution()    
    print(f"Question : {list}")
    res = sl.merge_intervals(list)
    print(res)

if __name__ == "__main__":
    main()