# Dynamic Programming
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, n+2, ... n]
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

