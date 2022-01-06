# Time Complexity: O(n)
from typing import List

class Solution:
    def can_jump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


sl = Solution()
nums = [2, 3, 1, 1, 4]
print(sl.can_jump(nums))
