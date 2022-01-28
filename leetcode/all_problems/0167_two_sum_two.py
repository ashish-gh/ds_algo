from typing import List


class Solution:
    def two_sum_ii(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l -= 1
            else:
                return [l + 1, r + 1]


def main():
    sl = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sl.two_sum_ii(nums, target))


main()
