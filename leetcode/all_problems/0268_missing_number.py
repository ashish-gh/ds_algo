from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        # res = []
        # for i in range(0, len(nums)):
        #     if i not in nums:
        #         res.append(i)
        # return res

        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res


def main():
    sl = Solution()
    nums = [1, 0]
    print(sl.missing_number(nums))


main()
