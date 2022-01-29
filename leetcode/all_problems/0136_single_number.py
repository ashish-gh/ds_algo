from typing import List


class Solution:
    def single_number(self, nums: List[int]):
        res = 0
        for num in nums:
            res = num ^ res
        return res


def main():
    sl = Solution()
    nums = [2, 2, 1]
    print(sl.single_number(nums))


main()
