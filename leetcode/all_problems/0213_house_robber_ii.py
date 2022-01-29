# Time complexity: O(n)
# Space complexity: O(1)


from re import M
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


def main():
    sl = Solution()
    print(sl.rob(nums=[2, 4, 5, 2]))
    ...


main()
