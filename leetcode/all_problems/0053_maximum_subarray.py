from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:

        cur_sum = 0
        max_sum = nums[0]
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(cur_sum, num)
        return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sl = Solution()
    print(sl.max_sub_array(nums=nums))


main()
